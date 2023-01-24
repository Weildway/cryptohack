from pwn import *
import json
import base64
import codecs

rot13 = lambda s: codecs.getencoder("rot-13")(s)[0]
s = remote("socket.cryptohack.org", 13377)

while True:

    json_string = s.recvuntil('\n').decode().strip()
    print(json_string)
    if 'flag' in json_string:
        break
    json_string_format = json.loads(json_string)

    current_type = json_string_format["type"]
    current_encrypted_text = json_string_format["encoded"]

    if current_type == "bigint":
        decrypted_text = b''.fromhex(current_encrypted_text.replace('0x', '')).decode()

    elif current_type == "rot13":
        decrypted_text = rot13(current_encrypted_text)

    elif current_type == "base64":
        decrypted_text = base64.standard_b64decode(current_encrypted_text).decode()

    elif current_type == "hex":
        decrypted_text = b''.fromhex(current_encrypted_text).decode()

    elif current_type == "utf-8":
        decrypted_text = ''.join([chr(c) for c in current_encrypted_text ])

    answer = '{"type": "' + current_type + '", "decoded": "' + decrypted_text + '"}'
    s.send((answer + '\n'))
    print(answer)
