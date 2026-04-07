import random

from hw2.TravellingSalesmanProblem.solvers.hillclimbing.simple_hillclimbing import SegmentReversalHillclimbing


class SimulatedAnnealing(SegmentReversalHillclimbing):
    def __init__(self, problem, iterations, climbers):
        super().__init__(problem, iterations, climbers)
        self._tabu = set()

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
                else:
                    r = random.random()
                    chance = float(i / self._iterations)
                    # print(r, chance)
                    if r**2 > chance:
                        # print("restart")
                        candidates[j] = self.generate_random()
                        f = self.fitness(candidates[j])

                self._best_values[j].append(f)

        return self._best_values

    # def solve(self):
    #     candidates = self.generate_climbers()
    #
    #     for i in range(self._climbers):
    #         self._best_values[i] = []
    #         f = self.fitness(candidates[i])
    #         self._best_values[i].append(f)
    #         t = tuple(candidates[i])
    #         self._tabu.add(t)
    #
    #     for i in range(self._iterations):
    #         for j in range(self._climbers):
    #             c, f = self.climb(candidates[j])
    #
    #             if c is not None:
    #                 candidates[j] = c
    #             else:
    #                 r = random.random()
    #                 chance = i / self._iterations
    #                 if r > chance:
    #                     candidates[j] = self.generate_random()
    #                     f = self.fitness(candidates[j])
    #
    #             self._best_values[j].append(f)
    #
    #     return self._best_values