import random

from hw2.TravellingSalesmanProblem.solvers.hillclimbing.hillclimbing import HillClimbing

class TabuSearchHillClimbing(HillClimbing):
    def __init__(self, problem, iterations, climbers):
        super().__init__(problem, iterations, climbers)
        self._tabu = set()

    def solve(self):
        candidates = self.generate_climbers()

        for i in range(self._climbers):
            self._best_values[i] = []
            f = self.fitness(candidates[i])
            self._best_values[i].append(f)
            t = tuple(candidates[i])
            self._tabu.add(t)

        for i in range(self._iterations):
            for j in range(self._climbers):
                c, f = self.climb(candidates[j])

                if c is not None:
                    t = tuple(c)
                    self._tabu.add(t)
                    candidates[j] = c

                self._best_values[j].append(f)

        return self._best_values

    # from SegmentReversalHillClimbing
    def generate_neighbors(self, candidate):
        neighbors = []
        for i in range(len(candidate)):
            c = candidate.copy()
            r = random.randint(0, len(candidate) - 1)
            while r == i:
                r = random.randint(0, len(candidate) - 1)

            a = min(i, r)
            b = max(i, r)
            segment = c[a:b]
            segment.reverse()
            c = c[:a] + segment + c[b:]

            t = tuple(c)
            if t not in self._tabu:
                neighbors.append(c)

        return neighbors