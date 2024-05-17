dlugosc_listy:: [Int]->Int
dlugosc_listy [] = 0
dlugosc_listy (x:t) = 1 + (dlugosc_listy t)