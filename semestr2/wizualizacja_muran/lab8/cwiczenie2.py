import numpy as np

A = np.array(([1, 1, 2],
              [2, 1, 0],
              [4, 1, 2]))

B = np.array(([2, 5, 7],
              [2, 8, 0],
              [4, 3, 1]))

C = np.array(([1],
              [2],
              [4]))

D = np.array((2, 5, 7))

E = np.array(([1, 5],
              [2, 1]))

F = np.array(([2, 1],
               [2, 8]))

print(A + B)
print(A * B)

print(A)
print(A.transpose())
print(A.conjugate())
print(A**5)
print(np.linalg.det(B))
print(C)
print(D)
print(C * D)
print(D * C)
print(C + D)
print(E / F)
print(E // F)
print(E % F)
