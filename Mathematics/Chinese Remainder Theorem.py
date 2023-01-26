M = 935
a = [5, 11, 17]
r = [2, 3, 5]
n = 3
m = [0] * n
minv = [0] * n
sum = 0
"""
x ≡ r1 mod a1
x ≡ r2 mod a2
...
x ≡ rn mod an
1) compute M=a1*a2*...an
2) find mi=M/ai
3) calculate inverse minvi for each mi
4) SUM for each i in (0,n): mi*ri*minvi
"""
for i in range(3):
    m[i] = M // a[i]
    minv[i] = pow(m[i], a[i] - 2, a[i])
    sum += m[i] * minv[i] * r[i]
print(sum % M)
