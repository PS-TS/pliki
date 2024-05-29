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

-- [1,2,3,4]=1:(2:(3:(4:[])))
-- 1:[2,3]=[1,2,3]
-- [1,2]++[6,7]=[1,2,6,7]
-- ['a','b','c','d']!!0='a'

-- (3+4*5:4:[6,[2],3])!!lenght[2,3,4] = [2]
-- reverse odwraca liste
-- tail zwraca ogon
-- length dlugosc
-- (reverse[5,2,1,7]++tail[2,3])!!head[1,1,3] = 1

-- kwadrat_lista (def. rekurencyjna)
kwadrat x=x*x
kwadrat_lista::[Int]->[Int]
kwadrat_lista[]=[]
kwadrat_lista(x:xs)=(kwadrat x):(kwadrat_lista xs)

mniej x=x-1
listao1::[Int]->[Int]
listao1[]=[]
listao1(x:xd)=(mniej x):(listao1 xd)

razy3 x=x*3
listarazy3::[Int]->[Int]
listarazy3[]=[]
listarazy3(x:xa)=(razy3 x):(listarazy3 xa)

dlugosclista::[Int]->Int
dlugosclista[]=0
dlugosclista(x:t)=1+dlugosclista t

listailoczyn::[Int]->Int
listailoczyn[x]=x
listailoczyn(x:t)=x*listailoczyn t

fun::[Int]->Int
fun[]=5
fun(x:y)=x-fun y

-- [10,7..2]=[10,7,4]
-- fun[10,7,4]=10-fun[7,4]=10-(7-fun[4])=10-(7-(4-5)))=2
-- reverse[1,2,3]->[3,2,1]

ostatni::[Int]->Int
ostatni xs=head(reverse xs)

usunostatni::[Int]->[Int]
usunostatni xs=reverse(tail(reverse xs))

konkatenacja::[Int]->[Int]->[Int]
konkatenacja xs ys=xs++ys
-- rekurencyjna
konkatenacja2 [] l2=l2
konkatenacja2 (h:t) l2 =h:(konkatenacja t l2)

-- [x*x|x<-[1..10],even x] = [4,16,36,64,100]
-- [y'mod'3|y<-5..10] = [2,0,1,2,0,1]
-- [a*b|(a,b)<-[(1,2),(2,3),(3,4)]] = [2,6,12]
-- [(x,y)|x<-[1,2],y<-[3,4]] = [(1,3),(1,4),(2,3),(2,4)]
-- [x|x<-[1..12],y<-[1..12],x*y==12] = [1,2,3,4,6,12]
-- [x|x<-[-5,2,3,-2], x>0] = [2,3]
-- [(x,y)|x<-[1..3],y<-[x..3]] = [(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]
-- [(x,y)|x<-[1..3],y<-[1..x]] = [(1,1),(2,1),(2,2),(3,1),(3,2),(3,3)]
-- [(x-y)|x<-[1..3],y<-[1..x]] = [0,1,0,2,1,0]

listamniejsza1::[Int]->[Int]
listamniejsza1 xs = [x-1|x<-xs]

mniejsze1 x = x-1
kolejnemniejszeo1::[Int]->[Int]
kolejnemniejszeo1 xs = map mniejsze1 xs


