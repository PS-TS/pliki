def dodaj_element(krotka, element):
    nowa_krotka = krotka + (element,)
    return nowa_krotka


def usun_element(krotka, element):
    lista = list(krotka)
    if element in lista:
        lista.remove(element)
    nowa_krotka = tuple(lista)
    return nowa_krotka


def usun_powtorzenia(lista):
    nowa_lista = []
    for element in lista:
        if element not in nowa_lista:
            nowa_lista.append(element)
    return nowa_lista

krotka1 = (1,2,3,4,5,6,1)
element = "x"
element1 = 3
print(dodaj_element(krotka1,element))
print(usun_element(krotka1,element1))
print(usun_powtorzenia(krotka1))