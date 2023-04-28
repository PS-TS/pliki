import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris.data', header = None)
x= df[0]
y = df[1]
data = { 'a': x, 'b': y,'c': np.random.randint(0,50,150), 'd': np.abs(df[0]-df[1])}

plt.scatter('a','b', c = 'c', s = 'd', data=data)



plt.xlabel('x')
plt.ylabel('f(x)')


plt.show()