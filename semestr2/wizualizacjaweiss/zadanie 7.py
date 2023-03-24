import numpy as np


def func(n):
    macierz = np.zeros((n,n))
    macierz = np.diag([2 for i in range(n)])

    macierz[:-1, 1:] = np.diag([2 * 2 for i in range(n - 1)])
    macierz[1:,:-1] = np.diag([2 * 2 for i in range(n - 1)])
    macierz[:-2, 2:] = np.diag([2 * 3 for i in range(n - 2)])
    macierz[2:, :-2] = np.diag([2 * 3 for i in range(n - 2)])

    print(macierz)


func(3)
