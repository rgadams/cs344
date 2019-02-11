"""
This module implements local search on a simple abs function variant.
The function is a linear function  with a single, discontinuous max value
(see the abs function variant in graphs.py).

@author: kvlinden
@version 6feb2013
"""
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math


class SineVariant(Problem):
    """
    State: x value for the sine function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta
        self.best_x = initial
        self.best_val = 0

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        val = math.fabs(x * (math.sin(x)))
        if val > self.best_val:
            self.best_val = val
            self.best_x = x
        return val


if __name__ == '__main__':
    # Formulate a problem with a 2D hill function and a single maximum value.
    maximum = 30
    initial = randrange(0, maximum)
    d = 2.0
    p = SineVariant(initial, maximum, delta=d)
    print('Initial                      x: ' + str(p.initial)
          + '\t\tvalue: ' + str(p.value(initial))
          )

    # Solve the problem using hill-climbing.
    hill_solution = hill_climbing(p)
    hs_max = p.best_x
    for y in range(4):
        hs = SineVariant(hs_max, maximum, delta=d)
        hs_max = hs.best_x
        hill_solution = hill_climbing(hs)
    print('Hill-climbing solution       x: ' + str(hill_solution)
          + '\tvalue: ' + str(hs.value(hill_solution))
          )

    # Solve the problem using simulated annealing.
    annealing_solution = simulated_annealing(
        p,
        exp_schedule(k=20, lam=0.005, limit=1000)
    )
    as_max = p.best_x
    for z in range(4):
        annsol = SineVariant(as_max, maximum, delta=d)
        as_max = annsol.best_x
        annealing_solution = simulated_annealing(
            annsol,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
    print('Simulated annealing solution x: ' + str(annealing_solution)
          + '\tvalue: ' + str(p.value(annealing_solution))
          )
