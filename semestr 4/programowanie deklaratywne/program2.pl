% wyznaczanie stopnia wielomianu
% o współczynnikach liczbowych

/* 
Definicja: rekurencja strukturalna

1) st(x) = 1
st(c) = 0, gdzie c - liczba

2) Stopnie wielomianów złożonych określamy następująco:
 st(-W) = st(W),
st(W1+W2)=st(W1-W2)=max(st(W1),st(W2)),
st(W1*W2) = st(W1)+st(W2),
st(W^N)= st(W)*N (N-liczba naturalna, N>1)

*/



%st_wielomian(W,X,N)
% spełniony, gdy N jest stopniem wielomianu W
% zmiennej X o współczynnikach liczbowych

	st_wielomianu(X,X,1).
	st_wielomianu(C,_,0):-number(C).
	st_wielomianu(-W,X,N):-st_wielomianu(W,X,N).
	st_wielomianu(W1+W2,X,N):-st_wielomianu(W1,X,N1),st_wielomianu(W2,X,N2), N is max(N1,N2).
	st_wielomianu(W1-W2,X,N):-st_wielomianu(W1,X,N1),st_wielomianu(W2,X,N2), N is max(N1,N2).
	st_wielomianu(W1*W2,X,N):-st_wielomianu(W1,X,N1),st_wielomianu(W2,X,N2), N is N1+N2.
	st_wielomianu(W^N,X,N1):-integer(N),N>1,st_wielomianu(W,X,N2), N1 is N2*N.
	