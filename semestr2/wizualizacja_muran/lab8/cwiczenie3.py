import numpy as np

produkcjaSamochodow = np.array(([1, 'China', 0.56, 19.91],
                                [2, 'Japan', 8.1, 8.27],
                                [3, 'Germany', 5.3, 5.6],
                                [4, 'USA', 5.63, 4.25],
                                [5, 'South Korea', 2.36, 4.12],
                                [6, 'India', 0.53, 3.15],
                                [7, 'Brazil', 1.1, 2.31],
                                [8, 'Mexico', 0.99, 1.91],
                                [9, 'Spain', 2.28, 1.89],
                                [10, 'Russia', 0.94, 1.69]))

print('Państwo; 1999; 2014')
minMaxProdukcja = { '1999-min': produkcjaSamochodow[0],
                    '1999-max': produkcjaSamochodow[0],
                    '2014-min': produkcjaSamochodow[0],
                    '2014-max': produkcjaSamochodow[0]}

for row in produkcjaSamochodow:
    panstwo = row[1]
    stareDane = float(row[2])
    noweDane = float(row[3])

    if (stareDane < float(minMaxProdukcja['1999-min'][2])):
        minMaxProdukcja['1999-min'] = row

    if (stareDane > float(minMaxProdukcja['1999-max'][2])):
        minMaxProdukcja['1999-max'] = row

    if (noweDane < float(minMaxProdukcja['2014-min'][3])):
        minMaxProdukcja['2014-min'] = row

    if (stareDane > float(minMaxProdukcja['2014-max'][3])):
        minMaxProdukcja['2014-max'] = row

    procentowyWzrost = noweDane / stareDane
    print(f'W {panstwo} procentowy wzrost produkcji samochodów wynosi: {round(procentowyWzrost, 2)}')

print(f'Najmniejsza produkcja w 1999 roku była w {minMaxProdukcja["1999-min"][1]} i wynosiła {minMaxProdukcja["1999-min"][2]}')
print(f'Największa produkcja w 1999 roku była w {minMaxProdukcja["1999-max"][1]} i wynosiła {minMaxProdukcja["1999-max"][2]}')
print(f'Najmniejsza produkcja w 2014 roku była w {minMaxProdukcja["2014-min"][1]} i wynosiła {minMaxProdukcja["2014-min"][3]}')
print(f'Największa produkcja w 2014 roku była w {minMaxProdukcja["2014-max"][1]} i wynosiła {minMaxProdukcja["2014-max"][3]}')
