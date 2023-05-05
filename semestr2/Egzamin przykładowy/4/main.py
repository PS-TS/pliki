import numpy as np
import matplotlib.pylab as plt

#prepare data
x = np.linspace(5, 15, 100)
y1 = x+4
y2 = -3*x+30
y3 = -3*x-5



fig, axs = plt.subplots()

plt.grid(which="both")

#axs.set_xlim([5, 15])
#axs.set_ylim([-10, 10])
axs.plot(x, y1, ls='--', c="grey", label = "x+4")
axs.plot(x, y2, ls='-.', c="red", label = "-3*x+30")
axs.legend(loc='lower center')
axs.set_xlabel("oś pozioma")
axs.set_ylabel("oś pionowa po lewej stronie")
#xtics = np.linspace(-10, 10, 0.5)
#axs.set_xticklabels(xtics)


ax2 = axs.twinx()
#ax2.set_ylim([-50, -25])
ax2.plot(x, y3, ls="dotted", c = "red", label = "-3*x-5")
ax2.legend(loc='center right')
ax2.yaxis.label.set_color('red')
ax2.set_ylabel("oś pionowa po prawej stronie")

plt.title("Wykresy - kilka")



plt.show()