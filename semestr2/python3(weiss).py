#zad1
def monotonicznosc(a):
    if(a>0):
        print("rosnaca")
    elif(a<0):
        print("malejaca")
    else:
        print("stala")   
print(monotonicznosc(0))

#zad2
def polozenie(a1, a2):
    if(a1==a2):
        print("rownolegle")
    elif(a1*a2==-1):
        print("prostopadla")
    else:
        print("inna")
print(polozenie(2,-0.5))

#zad3
import math
def przeciwprostakatna(a,b):
    return math.sqrt((a*a)+(b*b))
print(przeciwprostakatna(3,4))

#zad4
def sumaciagu(a1=1,r=1,ile=10):
    return ((2*a1)+((ile-1)*r)*ile)/2
print(sumaciagu())

#zad5
import copy
x = ["jeden","dwa"]
def dodajznak(lista):
    for i in range(len(lista)):
        lista[i]=lista[i]+'!'
def dodajnowyznak(lista):
    nowalista=copy.deepcopy(lista)
    for i in range(len(lista)):
        nowalista[i]=lista[i]+'!'
    return nowalista
print(x)
print(dodajnowyznak(x))
dodajznak(x)
print(x)

#zad6
import random
def guess_the_number():
    punkty=0
    x=0
    y=0
    for i in range(5):
        print("podaj liczbe")
        x=round(random.random()*9+1)
        y=input()
        if x==y:
            punkty=punkty+10
            print("dobrze, +10")
        else:
            punkty=punkty-1
            print("zle, -1")
    return punkty
print("Wynik:",guess_the_number())

#zad7
def dr(liczba):
    suma=0
    while (int(liczba)>0):
        suma=suma+liczba%10
        liczba=int(liczba/10)
    return suma
print(dr(1234))

#zad8
import random
def multipli_game():
    dobrze=0 
    zle=0 
    wpisana=0 
    z1=0 
    z2=0
    for i in range(10):
        z1=int(random.random()*9+1)
        z2=int(random.random()*9+1)
        print("Pytanie",i+1,":",z1,"x",z2,"=")
        wpisana=eval(input())
        if(wpisana==(z1*z2)):
            dobrze=dobrze+1
            print("dobrze")
        else:
            zle=zle+1
            print("zle, poprawna odpowiedz to:", z1*z2)
    print("Koniec")
    print("Dobrze",dobrze)
    print("Zle",zle)
multipli_game()
#zad9
def drukA(rozmiar):
    print('drukowanie...')
    for i in range(rozmiar):
        if(i==0):
            print((rozmiar-1)*' ','*',sep='')
        elif i==int(rozmiar/2):
            print((rozmiar-1-i)*' ',(2*i+1)*'*',sep='')
        else:
            print((rozmiar-1-i)*' ','*',(2*i-1)*' ','*',sep='')
drukA(5)
