################################ zad 1
zdanie = input()
print(zdanie.count(" "))
################################ zad 2
tekst = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
x = tekst.split(' ')
print(x)
################################ zad 3
# == != > >= < <=
################################ zad 4
i = eval(input())
if i<0:
    i=-i
print(i)
################################ zad 5
a = eval(input())
b = eval(input())
c = eval(input())
if a>0 and a<=10:
    print("a w przedziale")
else:
    print("pierwszy warunek niespełniony")
if a>b or b>c:
    print("a > b lub b > c")
else:
    print("drugi warunek niespełniony")
################################ zad 6
for i in range(51):
    if i%5==0:
        print(i)
################################ zad 7
tekst=input()
lista = tekst.split(' ')
tablica = [int(x) for x in lista]
for j in range(len(tablica)):
    print(tablica[j]**2)
################################ zad 8
liczbastr = input()
suma=0
for x in range(len(liczbastr)):
    suma=suma+int(liczbastr[x])
print(suma)
################################ zad 9
tab = []
x=""
while x!="end":
    x = input()
    if x.isdigit():
        tab.append(int(x))
    print(tab)
print("wynik:",tab)
################################ zad 10
wys = 0
while wys>10 or wys<1:
    wys = eval(input())
for i in range(wys+1):
    print('A'*i)
################################ zad 11
x=0
while x<2 or x>9:
    x = eval(input())
if x%2==0:
    x-=1
liczba=1
spacja=round(x/2)
spadek=0
print("-"*10)
for i in range(x):
    print(" "*spacja+"o"*liczba)
    if liczba==x:
        spadek=1
    if spadek==0:
        liczba+=2
        spacja-=1
    else:
        liczba-=2
        spacja+=1
print("-"*10)
