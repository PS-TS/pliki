--kwadrat_lista (definica rekurencyjna)

kwadrat  x=x*x
kwadrat_lista::[Int]->[Int]
--warunek zakończenia rekurencji
kwadrat_lista []=[]
kwadrat_lista (x:xs)=(kwadrat x):(kwadrat_lista xs)