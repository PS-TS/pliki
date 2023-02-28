set = {"Polska","Niemcy","USA","Hiszpania","Francja"}
set.append("Portugalia")

set.add("Portugalia")
print(set)
{'Portugalia', 'USA', 'Hiszpania', 'Polska', 'Niemcy', 'Francja'}
set.add("Polska")
print(set)
{'Portugalia', 'USA', 'Hiszpania', 'Polska', 'Niemcy', 'Francja'}
set.remove("Portugalia")
print(set)
{'USA', 'Hiszpania', 'Polska', 'Niemcy', 'Francja'}
set1 = {"USA", "Kanada", "Meksyk"}
set2 = {"Chiny", "Japonia", "Polska"}
kraje = set.union(set1, set2)
print(kraje)
{'Japonia', 'Polska', 'Chiny', 'Niemcy', 'Kanada', 'USA', 'Meksyk', 'Hiszpania', 'Francja'}
kraje = set.intersection(set1, set2)
print(kraje)
set()
kraje2 = set.difference(set1)
print(kraje2)
{'Polska', 'Francja', 'Niemcy', 'Hiszpania'}
x = {"Polska", "Niemcy"}
y = {"Polska", "Niemcy", "Szwecja", "Norwegia"}
if x.issubset(y):
    print("Zbiór x jest podzbiorem zbioru y")
else:
    print("Zbiór x nie jest podzbiorem zbioru y")

krotka = (1, "hello", 3.14, True, [1,2,3], {"key": "value"}, 'a')
print(krotka)

krotka[2] = 2.71

print(krotka[3])
True
print(krotka[3:6])
(True, [1, 2, 3], {'key': 'value'})
print(krotka[-3])
[1, 2, 3]
