import requests

source = "https://aes.cryptohack.org/block_cipher_starter/"

# sending request and receiving cipher text from the source
r = requests.get(f"{source}encrypt_flag")
info = r.json()
ciphertext = info["ciphertext"]
print("Ciphertext received: ", ciphertext)

# sending request and decrypting the cipher text
r = requests.get(f"{source}decrypt/{ciphertext}")
info = r.json()
plaintext = info["plaintext"]
print("Plaintext received: ", plaintext)
print("Flag converted: ", bytes.fromhex(plaintext))
