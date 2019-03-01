'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013

Modified by Roy Adams on 3/1/19 for CS344 at Calvin College for a cancer model.
'''

from probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2})
    ])

# P(C|T1,T2) = a * P(T1,T2|C)*P(C) = a * P(T1|C) * P(T2|C) * P(C) = a * 0.9 * 0.9 * 0.01 = <0.17, 0.83>
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
#print(elimination_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

# P(C|T1,-T2) = a * P(T1,-T2|C)*P(C) = a * P(T1|C) * P(-T2|C) * P(C) = a * 0.9 * 0.2 * 0.01 = <0.00565, 0.99435>
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())
#print(elimination_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

# These results make sense because the probability of having cancer in the first place is 0.01.
# Having one failed test makes us 99.4% sure that the person does not have cancer.