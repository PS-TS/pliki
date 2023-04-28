import matplotlib.pyplot as plt
import numpy as np

x =np.arange(0,30,0.1)
plt.plot(x,np.sin(x+np.pi)+2, label = 'sinx')
plt.plot(x,np.sin(x),label = 'sinx')

plt.axis([0,30,-1,3])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.show()