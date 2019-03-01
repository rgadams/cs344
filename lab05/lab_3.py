'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013

Modified by Roy Adams on 3/1/19 for CS344 at Calvin College for a happiness model.
'''

from probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
happy = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1}),
    ])

# Since these variables are independent, P(R|S) = P(S) = <0.01, 0.99>
print(enumeration_ask('Raise', dict(Sunny=T), happy).show_approx())
#print(elimination_ask('Raise', dict(Sunny=T), happy).show_approx())

print(enumeration_ask('Happy', dict(Raise=T), happy).show_approx())

# P(R|S,H) = a * P(H|S,R)*P(R) = a * < 1.0 * 0.01, 0.7 * 0.99 > = <0.014, 0.986>
print(enumeration_ask('Raise', dict(Sunny=T, Happy=T), happy).show_approx())
#print(elimination_ask('Raise', dict(Sunny=T, Happy=T), happy).show_approx())

print(enumeration_ask('Raise', dict(Happy=T), happy).show_approx())
#print(elimination_ask('Raise', dict(Happy=T), happy).show_approx())

print(enumeration_ask('Raise', dict(Sunny=F, Happy=T), happy).show_approx())
#print(elimination_ask('Raise', dict(Sunny=F, Happy=T), happy).show_approx())

# These answers make sense since it is so unlikely that Raise is true. If someone is happy it is much more likely due
# to it being sunny than being from a raise. However, if it is not sunny and someone is happy then the probability of
# having gotten a raise goes up.
