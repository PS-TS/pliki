% kwadrat listy (+l1,?l2).
% spełniony, gdy elementy listy L2 są kwadratami
%elementów listy l1; lista L1 jest listą liczbową
%ograniczenia l1 i l2 są listami liczbowymi
%-------------------------------------------
%warunek kończący rekurencję: kwadrat listy pustej jest listą pustą

kwadrat_listy([],[]).

%rekurencja:

kwadrat_listy([H1|T1],[H2|T2]):- H2 is H1*H1, kwadrat_listy(T1,T2).


%podwojenie(=l1,?l2).
%spełniony, gdy elementy listy l2 są podwojonymi elementami l1
%np. L1=[a,b], L2=[a,a,b,b]
%-------------------------------------------

%warunek kończący rekurencję
podwojenie([],[]).

%rekurencja
podwojenie([H1|T1],[H1,H1|T2]):-podwojenie(T1,T2).



%lista_mniejszao2(L1,L2) - spełniony, kiedy elementy listy L2 są odpowiednimi elementami L1 pomniejszonymi o 2


lista_mniejszao2([],[]).

lista_mniejszao2([H1|T1],[H2|T2]):- H2 is H1-2, lista_mniejszao2(T1,T2).


%lista_razy5(L1,L2), który jest spelniony, gdy elementy listy L2 są odpowiednimi elementami listy L1 pomnożonymi przez 5

lista_razy5([],[]).
lista_razy5([H1|T1],[H2|T2]):- H2 is H1*5, lista_razy5(T1,T2).


%liczba_elem(L,N) - spełniony, gdy N jest liczbą elementów listy L.

liczba_elem([],0).
liczba_elem([H|T],N1):- liczba_elem(T,N), N1 is N+1.


%element(E,L) - spełniony, gdy E jest elementem listy L.

element(E,[E|T]).
element(E,[H3|T3]):- element(E,T3). 