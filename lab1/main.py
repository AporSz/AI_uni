## you have n objects with weight and value
## try to find a good solution to maximise the price of the total value of objects

## parameters:
##      nr of candidates

import csv
import random
import numpy as np

def get_nr_of_candidates():
    try:
        candidates = int(input('How many candidates would you like? '))
        if candidates < 1:
            print('Please enter a positive integer larger than 0')
            return get_nr_of_candidates()
        return candidates
    except ValueError as e:
        print(e)
        print('Please enter a NUMBER larger than 0')
        return get_nr_of_candidates()

def get_nr_of_problems():
    try:
        nr_of_problems = int(input('How many problems would you like? '))
        if nr_of_problems < 1:
            print('Please enter a positive integer larger than 0')
            return get_nr_of_problems()
        return nr_of_problems
    except ValueError as e:
        print(e)
        print('Please enter a NUMBER larger than 0')
        return get_nr_of_problems()

SIZE = 5
NR_OF_PROBLEMS = get_nr_of_problems()
NR_OF_CANDIDATES = get_nr_of_candidates()

def get_dataset(n):
    with open('./archive/knapsack_5_items.csv') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=',')
        i = 0
        problems = []
        for row in spamreader:
            weights_str = row['Weights'].strip("[]")
            prices_str = row['Prices'].strip("[]")
            capacity_str = row['Capacity']
            weights = [int(x) for x in weights_str.split()]
            prices = [int(x) for x in prices_str.split()]
            capacity = int(capacity_str)
            problems.append([weights, prices, capacity])
            i += 1
            if i == n:
                break

        return problems

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

def solve_problems(problems):
    for problem in range(len(problems)):
        print(f'Solution for problem nr.{problem+1}:')
        print(solve_with_random(problems[problem]))
        print('\n==============================================\n')

if __name__ == '__main__':
    problems_to_solve = get_dataset(NR_OF_PROBLEMS)
    solve_problems(problems_to_solve)