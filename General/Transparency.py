from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

key = RSA.importKey(open('transparency.pem').read())
derkey=key.exportKey(format='DER')
hashed = SHA256.new(derkey)
print(hashed.hexdigest())
