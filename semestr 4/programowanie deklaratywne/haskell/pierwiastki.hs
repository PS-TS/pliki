pierwiastki:: Float->Float->Float->String
pierwiastki a b c
 |b*b-4*a*c>0 = "dwa pierwiastki"
 |b*b-4*a*c<0 = "brak pierwiastkow"
 |otherwise = "jeden pierwiastek"