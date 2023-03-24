import numpy as np


def func(lenght):
    vector = np.arange(lenght, 0, -1)
    return np.diag(vector)


print(func(4))
