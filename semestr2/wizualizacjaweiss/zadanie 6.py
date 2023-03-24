import numpy as np
w1 = np.array(list("malina"))
w2 = np.array(list("lizak"))
w3 = np.array(list("jagoda"))
macierz = np.zeros((6,6), dtype = str)

macierz[:,0] = w1
macierz[2,:-1] = w2
macierz[5, :] = w3[::-1]
print(w1)
print(w2)
print(w3)
print(macierz)
