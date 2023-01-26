"""
We say that an integer x is a Quadratic Residue if there exists
an a such that a^2 = x mod p. If there is no such solution,
then the integer is a Quadratic Non-Residue.
"""
p = 29
ints = [14, 6, 11]
for a in range(29):
    sq = pow(a, 2, 29)
    if sq in ints:
        print(sq, "is a quadratic residue")
        print(a, "is it's square root\n")
