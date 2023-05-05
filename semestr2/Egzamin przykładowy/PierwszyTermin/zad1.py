import pylab as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y1 = -x ** 3 + 3*x - 7
y2 = 4 * x + 6
y3 = 6 + 4 * x ** 3

plt.plot(x, y1, "--b", label="-x ** 3 + 3x - 7")
plt.plot(x, y2, "-g", label="4 * x + 6")
plt.plot(x, y3, "-.c", label="6 + 4 * x**3")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Wykresy")
plt.legend(loc="best")
plt.savefig("wykresy.pdf")
plt.show()

