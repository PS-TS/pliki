import matplotlib.pyplot as plt
import numpy as np

t =np.arange(1.,20.2,0.1)
plt.plot(t,1/t, label = 'f(x) = 1/x')
plt.axis([1,20,0,1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.show()
