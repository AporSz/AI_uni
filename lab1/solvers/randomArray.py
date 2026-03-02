import random
import numpy as np

from lab1.solvers.base import BaseSolver


class RandomSearchSolver(BaseSolver):
    def __init__(self, nr_of_candidates):
        self._nr_of_candidates = nr_of_candidates

    def solve(self, problem):
        best_solution = None
        max_value = 0
        size = len(problem)

        i = 0
        while i < self._nr_of_candidates:
            r = random.randint(1, (2 ** size ) - 1)
            random_array = np.unpackbits(np.uint8(r))[3:]

            value = problem.evaluate(random_array)

            if max_value < value and problem.is_feasible(random_array):
                max_value = value
                best_solution = [problem, random_array, max_value]

            i += 1

        return best_solution