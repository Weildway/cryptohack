import requests
import hashlib
from Crypto.Cipher import AES

source = "https://aes.cryptohack.org/passwords_as_keys/"

# sending request and receiving cipher text from the source
r = requests.get(f"{source}encrypt_flag")
info = r.json()
ciphertexthex = info["ciphertext"]
print("Ciphertext received: ", ciphertexthex)
ciphertext = bytes.fromhex(ciphertexthex)

with open('words.txt', 'r') as file:
    for word in file:
        word = word.strip()
        # generate keys from words in words.txt and encrypt it with AES's key
        try_key = hashlib.md5(word.encode()).digest()
        cipher = AES.new(try_key, AES.MODE_ECB)
        try:
            # decrypt and check if it starts with crypto{
            decrypted = cipher.decrypt(ciphertext)
            if b'crypto{' in decrypted:
                print("keyword: ", word)
                print(decrypted.decode())
        except ValueError as e:
            continue
