import numpy as np
import matplotlib.pylab as plt

#prepare data
labels = 37,47,49, 26, 23
sizes = [37,47,49, 26, 23]
leg = ['A', 'B', 'C', 'D', 'E']

#colors: https://matplotlib.org/stable/gallery/color/named_colors.html
colors = 'lime', 'brown', 'violet', 'slategrey', 'springgreen'

fig1, ax1 = plt.subplots()
#patches, texts = ax1.pie(sizes, labels=labels, startangle=90, colors = colors)
patches, texts = ax1.pie(sizes, labels=labels, startangle=90, colors = colors)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


#plt.legend(patches, leg, loc="upper right")
plt.legend(patches, leg, loc=(0.75, 0.75))

plt.title("Tytul", x=0.5, y=1.1)
plt.axis('equal')

plt.show()