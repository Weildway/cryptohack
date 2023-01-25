# In RSA the private key is the modular multiplicative inverse of the exponent e modulo the totient of N.
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
phi = (p - 1) * (q - 1)
# d = e^(-1) % phi
print(pow(65537, -1, phi))
# or
from Crypto.Util.number import inverse

print(inverse(65537, phi))
