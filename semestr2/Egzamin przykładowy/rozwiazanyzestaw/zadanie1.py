import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x = ['A', 'B', 'C', 'D', 'E']
y1 = [-35, -20, -50, -35, -45]
y2 = [38,38,40,35,37]
colors1 = ['yellowgreen', 'gold','blue','royalblue','darkmagenta']
colors2 = ['olive', 'mediumpurple', 'orange', 'green', 'olivedrab']
plt.subplot(1,2,1)
plt.title('Wykres 1')
plt.barh(x, y1, color = colors1)
plt.subplot(1,2,2)
plt.title('Wykres 2')
plt.barh(x,y2, color = colors2)
plt.show()
