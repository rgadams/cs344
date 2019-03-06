'''
This module implements the Bayesian network shown in the text, Figure 14.12a.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013

Modified by Roy Adams on 3/6/19 for CS344 at Calvin College.
'''

from probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
wet_grass = BayesNet([
    ('Cloudy', '', 0.5),
    ('Sprinkler', 'Cloudy', {T: 0.1, F: 0.5}),
    ('Rain', 'Cloudy', {T: 0.8, F: 0.2}),
    ('WetGrass', 'Sprinkler Rain', {(T, T): 0.99, (T, F): 0.9, (F, T): 0.9, (F, F): 0.0}),
    ])

# P(Cloudy) = <0.5, 0.5> This is directly from graph.
print(enumeration_ask('Cloudy', dict(), wet_grass).show_approx())

# P(Sprinkler|Cloudy) = <0.1, 0.9> This is directly from graph.
print(enumeration_ask('Sprinkler', dict(Cloudy=T), wet_grass).show_approx())

# P(Cloudy|Sprinkler, -Rain) = a * P(Sprinkler, -Rain|Cloudy) * P(Cloudy) = a * <0.1 * 0.2 * 0.5, 0.5 * 0.8 * 0.5> = <0.0476, 0.9524>
print(enumeration_ask('Cloudy', dict(Sprinkler=T, Rain=F), wet_grass).show_approx())

# P(WetGrass|Cloudy, Sprinkler, Rain) = <0.99, 0.01> This is directly from graph.
print(enumeration_ask('WetGrass', dict(Cloudy=T, Sprinkler=T, Rain=T), wet_grass).show_approx())

# P(Cloudy|-WetGrass) = a * P(-WetGrass|Cloudy) * P(Cloudy) =
# a * [P(-WetGrass|Sprinkler, Rain) * P(Sprinkler|Cloudy) * P(Rain|Cloudy)
#   + P(-WetGrass|Sprinkler, -Rain) * P(Sprinkler|Cloudy) * P(-Rain|Cloudy)
#   + P(-WetGrass|-Sprinkler, Rain) * P(-Sprinkler|Cloudy) * P(Rain|Cloudy)
#   + P(-WetGrass|-Sprinkler, -Rain) * P(-Sprinkler|Cloudy) * P(-Rain|Cloudy)] * P(Cloudy) =
# a * <[0.01 * 0.1 * 0.8 + 0.9 * 0.1 * 0.2 + 0.9 * 0.9 * 0.8 + 0.0 * 0.9 * 0.2] * 0.5,
#       <[0.01 * 0.5 * 0.2 + 0.9 * 0.5 * 0.8 + 0.9 * 0.5 * 0.2 + 0.0 * 0.5 * 0.8] * 0.5> = <0.639, 0.361>
print(enumeration_ask('Cloudy', dict(WetGrass=F), wet_grass).show_approx())
