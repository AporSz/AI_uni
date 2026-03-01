import csv

from lab1.models.models import KnapsackProblem


class DataLoader:
    def __init__(self, path, nr_of_problems):
        self._path = path
        self._nr_of_problems = nr_of_problems

    def get_data(self):
        with open(self._path) as csvfile:
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
                problems.append(KnapsackProblem(weights, prices, capacity))
                i += 1
                if i == self._nr_of_problems:
                    break

            return problems