lista_razy3:: [Int]->[Int]
lista_razy3 [] = []
lista_razy3 (x:t) = (3*x):(lista_razy3 t)