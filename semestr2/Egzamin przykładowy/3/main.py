import numpy as np
import matplotlib.pylab as plt

#prepare data



y1 = [14,24,17,24,21]
lab1 = 'A', 'B', 'C', 'D', 'E'
#colors: https://matplotlib.org/stable/gallery/color/named_colors.html
col1 = 'indigo', 'aquamarine', 'orange', 'coral', 'lime'
explode1 = (0.1, 0, 0, 0, 0)

y2 = [74,94,83,38,76]
lab2 = 74,94,83,38,76
#colors: https://matplotlib.org/stable/gallery/color/named_colors.html
col2 = 'pink', 'orangered', 'hotpink', 'slategrey', 'blue'
explode2 = (0.1, 0, 0, 0, 0)



fig, axs = plt.subplots(2,1)

#axs[0].pie(y1, colors = col1, labels= lab1, explode = explode1, autopct='%1.0f%%', labeldistance=1.2, shadow=True) 
axs[0].pie(y1, colors = col1, labels= lab1, explode = explode1, autopct='%1.0f%%', labeldistance=1.2) 
axs[0].set_title("Tytul 1")

axs[1].pie(y2, colors = col2, labels=lab2, explode = explode2, labeldistance=1.2) 
axs[1].set_title("Tytul 2")
axs[1].legend(lab1, loc=(-1.0, 0.0))

plt.savefig("plot.png", dpi=200)

plt.show()
