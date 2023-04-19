def iloczyn(*args):
    wynik = 1
    for liczba in args:
        wynik *= liczba
    return wynik


print("a")
print(iloczyn(5, 10, 19))
print(iloczyn(5, 6, 10))
print(iloczyn(5, 10, 15))


def sumpot(n, *args):
    wynik = 0
    for liczba in args:
        wynik += liczba ** n
    return wynik


print("b")
print(sumpot(5, 2, 5, 5))
print(sumpot(2, 5, 2))


def mean(*args):
    return sum(args) / len(args)


def gmean(*args):
    return sum(args) ** (1 / len(args))


print(mean(1, 2, 3, 4))
print(gmean(1, 2, 3, 4))


def dlstring(*args):
    wynik = 0
    for wyraz in args:
        wynik += len(wyraz)
    return wynik


print(dlstring("ala", "ma", "kota"))