import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dane = pd.read_excel("ceny21.xlsx")
maka = dane[dane["Rodzaje towarów"]== "mąka pszenna - za 1kg"]
kasza = dane[dane["Rodzaje towarów"]== "kasza jęczmienna - za 0,5kg"]
x = np.arange(0, len(maka["Wartość"]))
plt.scatter(x, maka["Wartość"], color="red",marker='*',label="mąka pszenna - za 1kg")
plt.scatter(x, kasza["Wartość"], color="blue",marker='^',label="kasza jęczmienna - za 0,5kg")
plt.title("Dane zboża")
plt.xticks(x,maka["Rok"])
plt.xlabel('Rok')
plt.ylabel('Cena w zł')
plt.annotate('Borys', xy=(4.5,2.2),color='black', fontsize=14)
plt.legend()
plt.savefig("zad2.png")
plt.show()