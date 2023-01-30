import numpy

v = [numpy.array([4, 1, 3, -1]), numpy.array([2, 1, -3, 4]), numpy.array([1, 0, -2, 7]), numpy.array([6, 2, 9, -5]), ]
u = [v[0]]
for vi in v[1:]:
    mi = [numpy.dot(vi, uj) / numpy.dot(uj, uj) for uj in u]
    u += [vi - sum([mij * uj for (mij, uj) in zip(mi, u)])]

print(round(u[3][1], 5))
