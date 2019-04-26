% Exercise 2.1

% 1. This unifies, since they are both the same atoms and do not even have to be instantiated.
% 2. This does not unify, they are different atoms.
% 8. This unifies, X = bread
% 9. This unifies, X = bread, Y = sausage
% 14. This does not unify, there is nothing that X can be that will make both sides the same complex term.

house_elf(dobby).
witch(hermione).
witch(’McGonagall’).
witch(rita_skeeter).
magic(X) :-  house_elf(X).
magic(X) :-  wizard(X).
magic(X) :-  witch(X).

% 1. Not satisfied, house_elf is not an atom so this returns an error.
% 2. Not satisfied, wizard is not an procedure so this returns an error.
% 3. Not satisfied, wizard is not an atom so this returns an error.
% 4. Not satisfied, I don't think Prolog likes quotes. It complained when when I loaded this file.
% 5. Hermione = dobby. It sees magic(X) :- house_elf(X) and also sees that house_elf(dobby). So it must see
% magic(Hermione) as dobby

% b) Prolog does not like multiple declarations with the same complex term on the left side of an inference. In the
% case that there is more, it will only allow unifications from the first such rule. If this were not the case, Hermione
% would never unify to dobby.

% c) Prolog does use resolution in inference. This means that when we get two clauses with some of the same atoms in it
% we can resolve the two clauses and get one new clause.