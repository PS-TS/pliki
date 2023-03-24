import numpy as np
def zad4(a,b):
    c = np.logspace(start=1, num=b, stop=b,base = a, dtype = int)
    print(c)

zad4(2,4)