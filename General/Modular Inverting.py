from Crypto.Util.number import *
"""
a^(p-1) = 1 (mod p)
a^(p-1) * a^-1 = a^-1 (mod p)
a^(p-2) * a * a^-1 = a^-1 (mod p)
a^(p-2) * 1 = a^-1 (mod p)
a^(p-2) = a^-1 (mod p)
"""
#using props of Fermat's little theorem
print(pow(3, 13-2) % 13)
#crypto func
inverse(3, 13)