% Problem 3.2
directlyIn(katarina, olga).
directlyIn(olga, natasha).
directlyIn(natasha, irina).

in(X, Y) :- directlyIn(X, Y).
in(X, Y) :- directlyIn(X, Z),
    in(Z, Y).

% Problem 4.5
tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

listtran([], []).
listtran([G|TG], [E|TE]) :- tran(G, E), listtran(TG, TE).

% Part b)
human(socrates).
mortal(X) :- human(X).

% A query mortal(socrates) returns true.