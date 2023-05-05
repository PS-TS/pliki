import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10000)

def randrange(n, vmin, vmax):
    return (vmax - vmin) * np.random.rand(n) + vmin

figura = plt.figure()
ax = figura.add_subplot(321, projection='3d')
bx = figura.add_subplot(322, projection='3d')
cx = figura.add_subplot(323, projection='3d')
dx = figura.add_subplot(324, projection='3d')
ex = figura.add_subplot(325, projection='3d')
n = 50
# wykres 1
for c, m, zlow, zhigh in [('r', 'o', -60, -25), ('b', '^', -50, -5)]:
     xs = randrange(n,23, 32)
     ys = randrange(n, 0, 86)
     zs = randrange(n, zlow, zhigh)
     ax.scatter(xs, ys, zs, c=c, marker=m)

# wykres 2
for c, m, zlow, zhigh in [('darkorange', 'p', -60, 25), ('springgreen', '1', -50, -5)]:
     xs = randrange(n,23, 32)
     ys = randrange(n, 0, 86)
     zs = randrange(n, zlow, zhigh)
     bx.scatter(xs, ys, zs, c=c, marker=m)

# wykres 3
for c, m, zlow, zhigh in [('slategrey', 'X', -60, 25), ('darkblue', '$...$', -50, -5)]:
     xs = randrange(n,23, 32)
     ys = randrange(n, 0, 86)
     zs = randrange(n, zlow, zhigh)
     cx.scatter(xs, ys, zs, c=c, marker=m)

#  wykres 4
for c, m, zlow, zhigh in [('gold', 'v', -98, -45), ('darkblue', '>', -70, -45)]:
     xs = randrange(n,23, 32)
     ys = randrange(n, 0, 86)
     zs = randrange(n, zlow, zhigh)
     dx.scatter(xs, ys, zs, c=c, marker=m)

# wykres 5
for c, m, zlow, zhigh in [('brown', '8', -98, -45), ('indigo', '*', -70, -45)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 86)
    zs = randrange(n, zlow, zhigh)
    ex.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
bx.set_xlabel('X Label')
bx.set_ylabel('Y Label')
bx.set_zlabel('Z Label')
cx.set_xlabel('X Label')
cx.set_ylabel('Y Label')
cx.set_zlabel('Z Label')
dx.set_xlabel('X Label')
dx.set_ylabel('Y Label')
dx.set_zlabel('Z Label')
ex.set_xlabel('X Label')
ex.set_ylabel('Y Label')
ex.set_zlabel('Z Label')

plt.show()
