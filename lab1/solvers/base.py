from abc import ABC, abstractmethod

from lab1.models.models import KnapsackProblem


class BaseSolver(ABC):
    @abstractmethod
    def solve(self, problem: KnapsackProblem):
        pass