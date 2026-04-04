from abc import ABC, abstractmethod

class BaseSolver(ABC):
    def __init__(self, problem):
        self._problem = problem

    def fitness(self, candidate):
        f = 0
        for i in range(len(candidate) - 1):
            f += self._problem[candidate[i]].distance(self._problem[candidate[i + 1]])

        f += self._problem[candidate[-1]].distance(self._problem[candidate[0]])

        return f

    def solve(self):
        pass