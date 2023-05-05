import numpy as np
import matplotlib.pylab as plt

#prepare data
x = [1,2,3,4,5]

x1 = [5,2,6,5,4]
y1 = [54,22,83,89,80]
#colors: https://matplotlib.org/stable/gallery/color/named_colors.html
col1 = 'indigo', 'aquamarine', 'orange', 'coral', 'lime'

x2 = [1, 4, 6, 8, 8]
y2 = [-53, -83, -77, -14, -76]
#colors: https://matplotlib.org/stable/gallery/color/named_colors.html
col2 = 'pink', 'orangered', 'hotpink', 'slategrey', 'blue'



fig, axs = plt.subplots(1,2)

hbar1 = axs[0].barh(x, y1, align='center', tick_label=x1, color = col1) 
axs[0].set_xlim([0,100])
axs[0].bar_label(hbar1, y1, fmt='%.2f', padding=2)
axs[0].set_title("Tytul 1")

hbar2 = axs[1].barh(x, y2, align='center', tick_label=x2, color = col2) 
axs[1].set_xlim([-100, 0])
axs[1].bar_label(hbar2, y2, fmt='%.2f', padding=2)
axs[1].set_title("Tytul 2")


plt.show()