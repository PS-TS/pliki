lista_mniejsza_o1:: [Int]->[Int]
lista_mniejsza_o1 [] =[]
lista_mniejsza_o1 (x:t)= (x-1):(lista_mniejsza_o1 t)