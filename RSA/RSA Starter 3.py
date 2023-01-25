"""
Based on the property of the Euler’s totient function in the prerequisite,
computing the Euler’s totient function for the product of two distinct prime numbers is actually very easy.
f(N)=f(pq)=f(p)f(q)=(p-1)(q-1)
"""
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
print((p - 1) * (q - 1))
