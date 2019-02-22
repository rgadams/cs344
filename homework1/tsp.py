from search import Problem, hill_climbing, simulated_annealing, exp_schedule
import random
import pandas as pd
import numpy as np
from copy import deepcopy

class TSP(Problem):

    """
    The Traveling Salesman Problem
    ------------------------------
    To initialize the TSP object you need a dataframe using the Pandas library
    cities = pd.DataFrame({
        0: {1: 10, 2: 1, 3: 4},
        1: {0: 10, 2: 5, 3: 1},
        2: {0: 1, 1: 5, 3: 7},
        3: {0: 4, 1: 1, 2: 7}
    })
    So the distance between city 0 and city 1 is 10
    State: Current ordering of the cities
    state = [0, 1, 2, 3]
    """

    def __init__(self, cities):
        self.cities = cities
        self.initial = list(range(len(cities)))
        self.n_cities = len(cities)

    def value(self, state):
        val = 0
        for i in range(len(self.cities)-1):
            # Add next city distance to result
            val += self.cities[state[i]][state[i+1]]
        # Last to first
        val += self.cities[state[len(self.cities)-1]][state[0]]
        return -val

    def actions(self, state):
        action_list = []
        for i in range(10):
            first = random.randint(1, self.n_cities - 1)
            # Make sure we are not swapping the same city
            while True:
                second = random.randint(1, self.n_cities - 1)
                if first != second:
                    break
            action_list.append([first, second])
        return action_list

    def result(self, state, action):
        new_state = state[:]
        new_state[action[0]], new_state[action[1]] = new_state[action[1]], new_state[action[0]]
        return new_state


def build_cities(n = 10):
    """
    build_cities creates a symmetric pandas dataframe with distances between 1 and 100.
    """
    cities = pd.DataFrame(np.zeros(shape=(n, n), dtype=np.int8))
    for i in range(n):
        for j in range(i, n):
            distance = random.randint(1, 100)
            cities[i][j] = distance
            cities[j][i] = distance
    return cities


if __name__ == "__main__":
    cities = build_cities(100)

    tsp = TSP(cities)

    hill_solution = hill_climbing(tsp)
    print('Hill-climbing solution       x: ' + str(hill_solution)
          + '\tvalue: ' + str(tsp.value(hill_solution))
          )

    annealing_solution = simulated_annealing(
        tsp,
        exp_schedule(k=20, lam=0.005, limit=1000)
    )
    print('Simulated annealing solution x: ' + str(annealing_solution)
          + '\tvalue: ' + str(tsp.value(annealing_solution))
          )

