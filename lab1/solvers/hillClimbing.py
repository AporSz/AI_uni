import random
import numpy as np

from lab1.solvers.base import BaseSolver

class HillClimbingSolver(BaseSolver):
    def __init__(self, nr_of_candidates):
        self._nr_of_candidates = nr_of_candidates

    def solve(self, problem):
        best_solution = None
        max_value = 0
        size = len(problem)

        i = 0
        while i < self._nr_of_candidates:
            r = random.randint(0, (2 ** size ) - 1)
            random_array = np.unpackbits(np.uint8(r))[3:]

            value = problem.evaluate(random_array)

            solution, value = self.hill_climbing(random_array, value, problem)

            if value > max_value:
                max_value = value
                best_solution = [str(problem), solution, value]

            i += 1

        return best_solution

    def generate_candidates(self, old_candidate):
        candidates = []

        for i in range(len(old_candidate)):
            candidate = old_candidate.copy()
            if candidate[i] == 0:
                candidate[i] = 1
            else:
                candidate[i] = 0

            candidates.append(candidate)

        return candidates

    def hill_climbing(self, old_candidate, old_max, problem):
        max_value = 0
        best_candidate = None

        candidates = self.generate_candidates(old_candidate)

        for candidate in candidates:
            value = problem.evaluate(candidate)

            if value > max_value and problem.is_feasible(candidate):
                max_value = value
                best_candidate = candidate

        if old_max >= max_value:
            return old_candidate, old_max

        return self.hill_climbing(best_candidate, max_value, problem)