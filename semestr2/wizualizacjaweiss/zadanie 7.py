import numpy as np

def func(n):
    macierz = np.zeros((n,n))
    for i in range(n):
        for j in range(n):

            macierz[i,j] = 2*(abs(i-j)+1)

    print(macierz)


func(8)
