from Crypto.Util.number import inverse

"""
588*x=665 mod p 
665*x=216 mod p
also there are 113 and 114 which difference is x
so 113*x=642mod p 114*x=851 mod p => x=851-642=209
"""

nums = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
maximum = max(nums)
x=209
for p in range(maximum + 1, 999):
    if (588 * x) % p == 665:
        print("crypto{%d,%d}" % (p, x))
