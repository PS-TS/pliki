abs:: Float->Float
abs x=if x<0 then (-x) else x

min:: Float->Float->Float
min a b = if a<b then a else b

abs2::Float->Float
abs2 x
 |x<0=(-x)
 |otherwise=x