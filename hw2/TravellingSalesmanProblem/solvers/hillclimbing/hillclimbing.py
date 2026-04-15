from abc import abstractmethod

from hw2.TravellingSalesmanProblem.solvers.basesolver import BaseSolver


class HillClimbing(BaseSolver):
    def __init__(self, problem, iterations = 100, climbers = 10):
        super().__init__(problem)
        self._iterations = iterations
        self._best_values = {}
        self._climbers = climbers


    def generate_climbers(self):
        climbers = {}
        for i in range(self._climbers):
            climbers[i] = self.generate_random()

        return climbers

    @abstractmethod
    def generate_neighbors(self, candidate):
        pass

    def climb(self, candidate):
        neighbors = self.generate_neighbors(candidate)

        m = self.fitness(candidate)
        best_candidate = None

        for n in neighbors:
            f = self.fitness(n)
            if f < m:
                m = f
                best_candidate = n

        return best_candidate, m

    def solve(self):
        candidates = self.generate_climbers()
        for i in range(self._climbers):
            self._best_values[i] = []
            f = self.fitness(candidates[i])
            self._best_values[i].append(f)

        for i in range(self._iterations):
            for j in range(self._climbers):
                c, f = self.climb(candidates[j])
                if c is not None:
                    candidates[j] = c

                self._best_values[j].append(f)

        return self._best_values
