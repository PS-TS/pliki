import matplotlib.pyplot as plt
import numpy as np

x =np.arange(0,30,0.1)
plt.plot(x,np.sin(x),label = 'sinx')
plt.plot(x,np.cos(x), label = 'cosx')
plt.axis([0,30,-1,1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.show()