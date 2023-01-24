def gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        d, u, v = gcd(b%a, a)
    return d, v-(b//a)*u, u


print(gcd(26513, 32321))

