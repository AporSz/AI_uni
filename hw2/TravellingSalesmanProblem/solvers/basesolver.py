from abc import ABC, abstractmethod
import random
import numpy as np

class BaseSolver(ABC):
    def __init__(self, problem):
        self._problem = problem

    def fitness(self, candidate):
        f = 0
        for i in range(len(candidate) - 1):
            f += self._problem[candidate[i]].distance(self._problem[candidate[i + 1]])

        f += self._problem[candidate[-1]].distance(self._problem[candidate[0]])

        return f

    def generate_random(self):
        numbers = np.arange(1, len(self._problem)+1).tolist()

        arr = []
        while len(numbers) != 0:
            n = random.randint(0, len(numbers)-1)
            arr.append(numbers[n])
            numbers.pop(n)

        return arr

    @abstractmethod
    def solve(self):
        pass