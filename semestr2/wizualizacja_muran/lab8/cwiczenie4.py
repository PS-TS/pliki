import numpy as np

statystyka = np.array((['Anna', 21, 'K', 65, 179, 'NIE'],
                       ['Zofia', 40, 'K', 80, 179, 'TAK'],
                       ['Sylwia', 13, 'K', 64, 151, 'NIE'],
                       ['Katarzyna', 31, 'K', 69, 177, 'TAK'],
                       ['Teresa', 34, 'K', 74, 170, 'NIE'],
                       ['Tomasz', 14, 'M', 61, 157, 'TAK'],
                       ['Cezary', 13, 'M', 66, 151, 'NIE'],
                       ['Zenon', 28, 'M', 61, 153, 'TAK'],
                       ['Filip', 20, 'M', 69, 160, 'NIE'],
                       ['Adrian', 15, 'M', 77, 160, 'TAK']))

imiona = np.array(sorted(statystyka[0:, 0]))
print(imiona)

okularnicy = statystyka[statystyka[0:, 5] == 'TAK'][0:, 0]
print(okularnicy)

sredniWiek = []
for row in statystyka:
    if row[2] == 'K' and 20 <= float(row[1]) and float(row[1]) <= 30:
        sredniWiek.append(row)
sredniWiek = np.array(sredniWiek)
print(sredniWiek)

sredniaWaga = []
for row in statystyka:
    if 60 <= float(row[3]) and float(row[3]) <= 80 and 160 <= float(row[4]) and float(row[4]) <= 180 and row[5] == 'NIE':
        sredniaWaga.append(row)
sredniaWaga = np.array(sredniaWaga)
print(sredniaWaga)

bmi = []
for row in statystyka:
    bmi.append(float(row[3])/(float(row[4])**2))
bmi = np.array(bmi)
print(bmi)
