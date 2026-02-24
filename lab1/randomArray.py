import random
import numpy as np


def calculate_value(weights, prices, random_array, capacity):
    current_capacity = 0
    current_value = 0
    for i in range(SIZE):
        if random_array[i] == 1:
            current_capacity += weights[i]
            current_value += prices[i]
    if current_capacity > capacity:
        return 0
    return current_value

def solve_with_random(problem):
    weights, prices, capacity = problem

    best_solution = None
    max_value = 0

    i = 0
    while i < NR_OF_PROBLEMS:
        r = random.randint(0, np.pow(2, SIZE) - 1)
        random_array = np.unpackbits(np.uint8(r))[3:]

        value = calculate_value(weights, prices, random_array, capacity)
        if value == 0:
            i -= 1

        if max_value < value:
            max_value = value
            best_solution = [random_array,weights,prices,max_value]

        i += 1

    return best_solution