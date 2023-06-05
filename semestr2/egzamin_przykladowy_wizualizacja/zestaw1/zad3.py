import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("wynagrodzenia21.csv",sep=';')
data_sorted = data.sort_values('2010')
cleaned = data.dropna()
warmińsko_mazurskie = data.loc[data['Województwo'] == 'WARMIŃSKO-MAZURSKIE', '2010':'2013'].values.flatten()
opolskie = data.loc[data['Województwo'] == 'OPOLSKIE', '2010':'2013'].values.flatten()
lata = ['2010', '2011', '2012', '2013']
plt.plot(lata, warmińsko_mazurskie,'r', label='Warmińsko-Mazurskie')
plt.plot(lata, warmińsko_mazurskie,'>')
plt.plot(lata, opolskie,'b', label='Opolskie')
plt.plot(lata, opolskie,'^')
plt.title('Wynagrodzenia w województwie Warmińsko-Mazurskim i Opolskim (2010-2013)')
plt.legend()
plt.xlabel('Lata')
plt.ylabel('Wynagrodzenie')
plt.savefig("zad3.webp")
plt.show()