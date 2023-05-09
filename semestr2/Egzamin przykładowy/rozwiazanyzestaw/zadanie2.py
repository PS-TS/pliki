import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('ceny4.xlsx')


print(df)
x = df['Rok'].values
y = df['Wartość'].values
plt.plot(x,y)
plt.text(2018,3.8,'09.05.2023')
plt.title('Cena ryżu w Polsce')
plt.savefig('wykres.jpg')
plt.show()
