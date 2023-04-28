xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

c = df.groupby(['Rok']).agg({'Liczba': ['sum']})
plt.subplot(1, 3, 3)
plt.xlabel('Rok')
plt.ylabel('Suma')
plt.title("Suma urodzonych dzieci w danym roku: ")
c.plot.bar(color=['black'])
plt.show()


#rymszewicz
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
a = df.groupby(['Plec']).agg({'Liczba':[sum]})
a.plot.bar()
b1 = df[df['Plec'] == 'K']
b1dane = b1.groupby(['Rok']).agg({'Liczba':[sum]})

b1dane.plot.bar()
c = df.groupby(['Rok']).agg({'Liczba': ['sum']})
c.plot.bar(color=['black'])





plt.xlabel('Rok')
plt.ylabel('Suma')
plt.title("Suma urodzonych dzieci w danym roku: ")

plt.show()
