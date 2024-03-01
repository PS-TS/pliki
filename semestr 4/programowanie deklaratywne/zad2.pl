%--------------------------lubi/2
lubi(marta, wino).
lubi(marta,mandarynki).
lubi(marta,tenis).
lubi(marta,kwiaty).
lubi(piotr,banany).
lubi(piotr, wino).
lubi(piotr,tenis).
lubi(jan,X):- lubi(piotr,X).
lubi(ania,X):- lubi(marta,X),lubi(jan,X).

%--------------------------lubi/2