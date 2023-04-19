def nrtel(**kwargs):
    for imie, nr in kwargs.items():
        print(f" {imie} ma numer {nr}")


nrtel(Tomek='234-211-423', Ania='433-233-422')


def wzrostwypalty(**kwargs):
    zarobek = list(kwargs.values())
    n = len(zarobek)
    mean = sum(zarobek) / n
    gmean = sum(zarobek) ** (1 / n)
    return mean, gmean


zarobki = {'St': 4000, 'Lu': 1500, 'Marz': 3500}
mean, gmean = wzrostwypalty(**zarobki)
print(f"Srednia aryt: {mean:.2f}")
print(f"Srednia geo: {gmean:.2f}")
zarobki2 = {'St': 1000, 'Lu': 2500, 'Marz': 3300, 'Kw': 10000}
mean2, gmean2 = wzrostwypalty(**zarobki2)
print(f"Srednia aryt: {mean2:.2f}")
print(f"Srednia geo: {gmean2:.2f}")