'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013

Modified by Roy Adams on 3/1/19 for CS344 at Calvin College.
'''

from probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# This is taken directly from the table for Alarm | Burglary, Earthquake
# P(A|B,-E) = <0.94, 0.06>
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
#print(elimination_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())

# This is a * (P(J|A)*P(A|B,-E)+P(J|-A)*P(-A|B,-E)) = a * (0.9*0.94+0.05*0.06) = <0.85, 0.15>
# a is our alpha normalizing term
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())
#print(elimination_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())

# a * (P(B)*P(E)*P(A|B,E)+P(B)*P(-E)*P(A|B,-E)) = a * (0.001*0.002*0.95 + 0.001*0.998*0.94) = <0.374, 0.626>
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
#print(elimination_ask('Burglary', dict(Alarm=T), burglary).show_approx())

# <0.284, 0.716>
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
#print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())