import numpy as np
def func(tab, kierunek = "poz"):
    dziel = tab.shape
    if (dziel[0]%2==0 and dziel[1]%2==0):


        a = dziel[0]
        b = dziel[1]
        if(kierunek == "poz"):

            tab1 = tab[:int(a/2), :]
            tab2 = tab[int(a/2):,:]

        elif(kierunek == "pion"):
            tab1= tab[:,:int(b/2)]
            tab2= tab[:,int(b/2):]

        print(tab1)
        print(tab2)
tablica = np.array([np.arange(4), np.arange(4)])

print(tablica)
func(tablica)
func(tablica, "pion")
