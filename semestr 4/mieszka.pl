%Ola, piotr karol na dworcowej
%Ania Pawel na ogrodowej
%Kamil i Gosia na irysowej
%marcin na tej co ola
%jezeli 2 na tej samej ulicy to sasiad
% mieszka(X,Y) - X mieszka na Y
% sasiedzi(X,Y) - X jest sasiadem Y

mieszka(ola,dworcowa).
mieszka(piotr,dworcowa).
mieszka(karol,dworcowa).
mieszka(ania,ogrodowa).
mieszka(pawel,ogrodowa).
mieszka(kamil,irysowa).
mieszka(gosia,irysowa).
mieszka(marcin,X):-mieszka(ola,X).
sasiedzi(X,Y):-mieszka(X,G),mieszka(Y,G),X\==Y.
