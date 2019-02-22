'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@modifiedBy: rga6
@version Jan 1, 2013
@modified: Feb 22, 2019
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

"""
P(Cavity|Catch) = P(Cavity ^ Catch) / P(Catch) 
= P(Cavity ^ Catch) / P(Cavity ^ Catch) v P(-Cavity ^ Catch)
= P(Cavity ^ Catch ^ Toothache) v P(Cavity ^ Catch ^ -Toothache) /
    [P(-Cavity ^ Catch ^ Toothache) v P(-Cavity ^ Catch ^ -Toothache) 
        v P(-Cavity ^ Catch ^ Toothache) v P(-Cavity ^ Catch ^ -Toothache)]
        
= 0.108 + 0.072 / 0.108 + 0.072 + 0.016 + 0.144 = 0.5294

P(-Cavity|Catch) = 1 - P(Cavity|Catch) = 0.4706
"""

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print("Cavity|Catch:", PC.show_approx())

Q = JointProbDist(['Coin1', 'Coin2'])
heads, tails = True, False

Q[heads, heads] = 0.25
Q[heads, tails] = 0.25
Q[tails, heads] = 0.25
Q[tails, tails] = 0.25

PC = enumerate_joint_ask('Coin2', {'Coin1': heads}, Q)
print("Coin2|Coin1:", PC.show_approx())
