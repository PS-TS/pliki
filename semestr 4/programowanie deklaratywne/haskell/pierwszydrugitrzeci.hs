--funkcje wyznaczające pierwszy, drugi i trzeci element trójki uporządkowanej
first::(a,b,c)->a
first(x,_,_)=x
second::(a,b,c)->b
second(_,y,_)=y
third::(a,b,c)->c
third(_,_,z)=z