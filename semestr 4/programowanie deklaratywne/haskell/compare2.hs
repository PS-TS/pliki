compare:: Ord a=>a->a->Ordering
compare x y
 |x<y = LT
 |x>y = GT
 |otherwise = EQ
