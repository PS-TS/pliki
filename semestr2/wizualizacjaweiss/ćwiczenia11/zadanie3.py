import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

figura = plt.figure()
ax = figura.add_subplot(321, projection='3d')
bx = figura.add_subplot(322, projection='3d')
cx = figura.add_subplot(323, projection='3d')
dx = figura.add_subplot(324, projection='3d')
ex = figura.add_subplot(325, projection='3d')
# wykres 1
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X,Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
figura.colorbar(surf, shrink=0.5, aspect=5)

# wykres 2
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X,Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

surf = bx.plot_surface(X, Y, Z, cmap=cm.summer, linewidth=0, antialiased=False)

bx.set_zlim(-1.01, 1.01)
bx.zaxis.set_major_locator(LinearLocator(10))
bx.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
figura.colorbar(surf, shrink=0.5, aspect=5)

# wykres 3
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X,Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

surf = cx.plot_surface(X, Y, Z, cmap=cm.YlGnBu, linewidth=0, antialiased=False)

cx.set_zlim(-1.01, 1.01)
cx.zaxis.set_major_locator(LinearLocator(10))
cx.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
figura.colorbar(surf, shrink=0.5, aspect=5)

# wykres 4
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X,Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

surf = dx.plot_surface(X, Y, Z, cmap=cm.Pastel1, linewidth=0, antialiased=False)

dx.set_zlim(-1.01, 1.01)
dx.zaxis.set_major_locator(LinearLocator(10))
dx.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
figura.colorbar(surf, shrink=0.5, aspect=5)

# wykres 5
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

surf = ex.plot_surface(X, Y, Z, cmap=cm.Wistia, linewidth=0, antialiased=False)

ex.set_zlim(-1, 1)
ex.zaxis.set_major_locator(LinearLocator(10))
ex.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
figura.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
