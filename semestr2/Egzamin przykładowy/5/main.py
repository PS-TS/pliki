import numpy as np
import matplotlib.pylab as plt

#prepare data
X = ['PL','DE','FR','SK']
x = np.arange(len(X))

y1 = [40, 25,42, 12 ]
col1 = 'red'

y2 = [45,30, 40, 45 ]
col2 = 'blue'

y3 = [32, 45, 45, 25]
col3 = 'grey'



fig, axs = plt.subplots()

hbar1 = axs.barh(x-0.2, y1, 0.2, align='center', color = col1) 
hbar1 = axs.barh(x, y2, 0.2, align='center', tick_label=X, color = col2) 
hbar1 = axs.barh(x+0.2, y3, 0.2,  align='center',  color = col3) 
axs.set_xlim([0,49])
axs.set_title("Wykres")
axs.xaxis.label.set_color('green')
axs.set_xlabel("podpis osi 2")
axs.yaxis.label.set_color('red')
axs.set_ylabel("podpis osi 1")
axs.grid(visible=True)

#plt.legend(patches, leg, loc="upper right")
plt.legend( ['A', 'B', 'C'], loc=(0.5, 0.75))


plt.show()