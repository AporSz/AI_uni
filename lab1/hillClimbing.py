import random
import numpy as np

from utils import calculate_value

def generate_candidates(old_candidate, size):
    candidates = []

    for i in range(size):
        candidate = old_candidate.copy()
        if candidate[i] == 0:
            candidate[i] = 1
        else:
            candidate[i] = 0

        candidates.append(candidate)
    
    return candidates

def hill_climbing(old_candidate, old_max, size, problem):
    max_value = 0
    best_candidate = None

    candidates = generate_candidates(old_candidate, size)

    for candidate in candidates:
        value = calculate_value(candidate, size, problem=problem)

        if value > max_value:
            max_value = value
            best_candidate = candidate

    if old_max >= max_value:
        return old_candidate, old_max

    return hill_climbing(best_candidate, max_value, size, problem)


def solve_with_hillclimbing(problem, nr_of_candidates, size):
    best_solution = None
    max_value = 0

    i = 0
    while i < nr_of_candidates:
        r = random.randint(0, np.pow(2, size) - 1)
        random_array = np.unpackbits(np.uint8(r))[3:]

        value = calculate_value(random_array, size, problem=problem)

        solution, value = hill_climbing(random_array, value, size, problem)

        if value > max_value:
            max_value = value
            best_solution = [problem, solution, value]

        i += 1

    return best_solution

