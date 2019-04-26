floats(X) :- weighsSameAsDuck(X).
madeOfWood(X) :- floats(X).
burns(X) :- madeOfWood(X).
witch(X) :- burns(X).

weighsSameAsDuck(woman).

% ?- witch(woman).
% true.
