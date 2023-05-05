import pylab as plt
import numpy as np
import pandas as pd


df = pd.read_excel('kina4.xlsx')
df.head()


dfG = df.groupby("Gestor")
dfG = dfG.sum()

plt.bar(x=dfG.index, height=dfG["Wartosc"])

plt.show()
