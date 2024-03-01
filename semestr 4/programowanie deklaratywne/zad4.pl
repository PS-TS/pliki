%lubi(X,Y) - spełniony, gdy X lubi Y.
% jarosz(X) - X jest jaroszem
% niepali(X) - X nie pali
% czyta(X) -  X czyta książki
% sport(X) - X uprawia sport
%---------------------------------
jarosz(ola).
jarosz(ewa).
jarosz(jan).
jarosz(pawel).
niepali(ola).
niepali(ewa).
niepali(jan).
czyta(ola).
czyta(iza).
czyta(piotr).
sport(ola).
sport(jan).
sport(piotr).
sport(pawel).
%---------------------------------

%---------------------------------lubi/2
lubi(ola,X):- jarosz(X),sport(X).
lubi(ewa,X):- jarosz(X),niepali(X).
lubi(iza,X):- czyta(X).
lubi(iza,X):- sport(X),niepali(X).
lubi(jan,X):- sport(X).
lubi(piotr,X):- jarosz(X),sport(X).
lubi(piotr,X):- czyta(X).
lubi(pawel,X):- jarosz(X),sport(X),czyta(X).
%---------------------------------lubi/2

