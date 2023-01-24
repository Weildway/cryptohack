import pwn

flagformat = b"crypto{"
#xor the result with the beginning of the flag
print(pwn.xor(bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'),flagformat))
#xor the result with the probable key
print(pwn.xor(bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'),b"myXORkey"))
