% Exercise 1.4

% fact that butch is a killer
killer(butch).
% facts that both mia is married to marsellus and vice versa.
married(mia, marsellus).
married(marsellus, mia).
% fact that zed is dead
dead(zed).

% IF person X gives mia a footMassage, marsellus will kill person X
kills(marsellus, X) :- footMassage(X, mia).

% If X is a goodDancer, mia loves X
loves(mia, X) :- goodDancer(X).

% If X is nutritious or tasty, jules will eat X
eats(jules, X) :- nutritious(X).
eats(jules, X) :- tasty(X).

% Exercise 1.5

wizard(ron).
hasWand(harry).
quidditchPlayer(harry).
wizard(X) :-  hasBroom(X),  hasWand(X).
hasBroom(X):-  quidditchPlayer(X).

% wizard(ron). Responds true
% witch(ron). Responds with undefined procedure witch/1
% wizard(hermione). Responds false
% witch(hermione). Responds with undefined procedure witch/1
% wizard(harry). Responds true
% wizard(Y). Y = ron
% witch(Y). Responds with undefined procedure witch/1

% Prolog never sees the keyword witch so it doesn't know what to do with it.
% harry hasWand and is a quidditchPlayer so he hasBroom by hasBroom(X) :- quidditchPlayer(X) and therefore he
% is a wizard by wizard(X) :-  hasBroom(X),  hasWand(X).
% wizard(Y) returns ron because ron is the first person declared as such.


% b)
% Prolog does use modus ponenes. We can see this in exercise 1.5.

% hasBroom(X):- quidditchPlayer(X).
% quidditchPlayer(harry).
% Therefore hasBroom(harry).

% c)
% Horn clauses are clauses that contain at most one positive literal. The resolution of two horn clauses is also a horn
% clause, which leads to greater efficiencies in theorem proving.

% d)
% In Prolog we TELL facts and then ASK questions (?-) based on the facts.


