import numpy as np
import math
def fibbonacii(n):
    tablica = np.arange(n)
    a = 1
    b = 1
    tablica[0] = a
    tablica[1] = b
    for i in range(n-2):
        tablica[i+2] = tablica[i+1] + tablica[i]
    tablica = tablica.reshape(int(math.sqrt(n)), int(math.sqrt(n)))
    print(tablica)



fibbonacii(25)
