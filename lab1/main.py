## you have n objects with weight and value
## try to find a good solution to maximize the price of the total value of objects

## parameters:
##      nr of candidates

import csv

from lab1.solvers.hillClimbing import HillClimbingSolver
from lab1.utils.data_loader import DataLoader
from lab1.utils.utils import get_nr_of_problems
from lab1.utils.utils import get_nr_of_candidates

SIZE = 5
NR_OF_PROBLEMS = get_nr_of_problems()
NR_OF_CANDIDATES = get_nr_of_candidates()

def solve_problems(problems):
    solver = HillClimbingSolver(NR_OF_CANDIDATES)
    for problem in range(len(problems)):
        print(f'Solution for problem nr.{problem+1}:')
        # print(solve_with_random(problems[problem], NR_OF_CANDIDATES, SIZE))
        print(solver.solve(problems[problem]))
        print('\n==============================================\n')

if __name__ == '__main__':
    dataloader = DataLoader('../lab1/data/knapsack_5_items.csv', NR_OF_PROBLEMS)
    problems_to_solve = dataloader.get_data()
    solve_problems(problems_to_solve)