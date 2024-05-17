--Ord - klasa typów dla których zefiniowane jest porównywanie
--compare - porównuje argumenty i zwraca wartosc LT,GT,EQ przy pomocy --strażników


compare:: Ord a=> a->a->Ordering 
compare x y
 |x<y = LT
 |x>y = GT
 |x==y=EQ