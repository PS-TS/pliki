--Ord - klasa typów dla których zefiniowane jest porównywanie
--compare - porównuje argumenty i zwraca wartosc LT,GT,EQ przy pomocy --strażników


compare:: Ord a=> a->a->Ordering 
compare x y = if x<y then LT else if x>y then GT else EQ
 