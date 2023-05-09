import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

odczyt = pd.read_csv("sport4.csv", delimiter= ";")
df = odczyt.filter(items = ['Nazwa','Gry zespołowe','Wartość'])
df = df[(df['Nazwa']== 'PODLASKIE') | (df['Nazwa'] == 'MAŁOPOLSKIE')]
x = df[df['Nazwa'] == 'PODLASKIE']['Gry zespołowe'].values

y1 = df[df['Nazwa'] == 'PODLASKIE']['Wartość']
y2 = df[df['Nazwa'] == 'MAŁOPOLSKIE']['Wartość']
width = 0.4
index = np.arange(4)
plt.bar(index-(width/2),y1,width = width, label = 'PODLASKIE', color = (0,0.5,0))
plt.bar(index+(width/2),y2,width = width, label = 'MAŁOPOLSKIE')
plt.xticks(index,x)
plt.legend()
plt.title("sport")

plt.show()
