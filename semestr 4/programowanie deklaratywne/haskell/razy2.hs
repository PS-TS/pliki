--f(x)=2*x
--razy_dwa :: Num a => a -> a
razy_dwa x = 2*x


--g(x) = x*x
kwadrat x = x*x


--h(x,y)=x^2+y^2
sum_kw x y = kwadrat x 
	   + kwadrat y

--pole kola o promieniu r 
pole_kola1 :: float -> float
pole_kola1 r = pi*r*r

pole_kola2 :: float -> float
pole_kola2 r = pi*kw
               where kw = r*r

pole_kola3 :: float -> float
pole_kola3 r = let kw = r*r
               in pi*kw