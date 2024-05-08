kwadrat::Float->Float
kwadrat x=x*x
pkolo r=pi*r*r
obkuli r=a*pi*sz where 
		a=4/3 
		sz=r*r*r
abs::Float->Float
abs x=if x<0 then (-x) else x
min:: Integer->Integer->Integer
min x y=if x>y then y else x

abs2::Float->Float
abs2 x
	|x<0 = (-x)
	|otherwise = x
	
sgn::Float->Float
sgn x=if x>0 then 1 else if x<0 then (-1) else 0

sgn2::Float->Float
sgn2 x
	|x>0 = 1
	|x<0 = (-1)
	|otherwise = 0
	
albo_albo1::(Bool,Bool)->Bool
albo_albo1 (p,q)= case (p,q) of (True,True)->False
				(True,False)->True
				(False,True)->True
				(False,False)->False
albo_albo2::Bool->Bool->Bool
albo_albo2 p q=if p==q then False else True

albo_albo3::Bool->Bool->Bool
albo_albo3 p q
	|p==q=False
	|otherwise=True
albo_albo4::Bool->Bool->Bool
albo_albo4 x y= x&&not y||not x&&y

imp::Bool->Bool->Bool
imp p q=if p==True&&q==False then False else True

test::Bool->Bool->Bool
test x y=if x==y then True else False

test1::Float->Float->Float
test1 x y
	|x>y = 1
	|x==y = 0
	|x<y = (-1)
 
sprawdz::Float->String
sprawdz x
	|x<0 = "liczba mniejsza od 0"
	|x>5 = "liczba wieksza od 5"
	|otherwise = "liczba z przedziału 0-5"

first::(a,b,c)->a
first(x,_,_)=x
second::(a,b,c)->b
second(_,y,_)=y
third::(a,b,c)->c
third(_,_,z)=z

-- klasa Ord
compare::Ord a=>a->a->Ordering
compare a b
	|a>b = GT
	|a<b = LT
	|otherwise = EQ
