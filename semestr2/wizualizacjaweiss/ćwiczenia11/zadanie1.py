import numpy as np
import matplotlib
import matplotlib.pyplot as plt

figura = plt.figure()
ax = figura.add_subplot(projection='3d')

z = np.linspace(0, 2*np.pi, 100)
x = np.sin(z)
y = np.cos(z) * 2

ax.plot(x, y, z, label='x = sin(z), y = 2*cos(z)')
ax.legend()
plt.show()
