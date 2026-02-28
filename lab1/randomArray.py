import random
import numpy as np

from utils import calculate_value

def solve_with_random(problem, nr_of_candidates, size):
    weights, prices, capacity = problem

    best_solution = None
    max_value = 0

    i = 0
    while i < nr_of_candidates:
        r = random.randint(1, (2 ** size )- 1)
        random_array = np.unpackbits(np.uint8(r))[3:]

        value = calculate_value(random_array, size, weights, prices, capacity)
        if value == 0:
            i -= 1

        if max_value < value:
            max_value = value
            best_solution = [random_array,weights,prices,max_value]

        i += 1

    return best_solution