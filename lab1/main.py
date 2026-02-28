## you have n objects with weight and value
## try to find a good solution to maximise the price of the total value of objects

## parameters:
##      nr of candidates

import csv

from hillClimbing import solve_with_hillclimbing
from utils import get_nr_of_problems
from utils import get_nr_of_candidates
from randomArray import solve_with_random

SIZE = 5
NR_OF_PROBLEMS = get_nr_of_problems()
NR_OF_CANDIDATES = get_nr_of_candidates()

def get_dataset(n):
    with open('./lab1/archive/knapsack_5_items.csv') as csvfile:
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

def solve_problems(problems):
    for problem in range(len(problems)):
        print(f'Solution for problem nr.{problem+1}:')
        # print(solve_with_random(problems[problem], NR_OF_CANDIDATES, SIZE))
        print(solve_with_hillclimbing(problems[problem], NR_OF_CANDIDATES, SIZE))
        print('\n==============================================\n')

if __name__ == '__main__':
    problems_to_solve = get_dataset(NR_OF_PROBLEMS)
    solve_problems(problems_to_solve)