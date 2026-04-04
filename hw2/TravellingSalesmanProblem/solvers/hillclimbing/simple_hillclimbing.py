import random

from hw2.TravellingSalesmanProblem.solvers.hillclimbing.hillclimbing import HillClimbing


class SimpleNeighborSwapHillclimbing(HillClimbing):
    def generate_neighbors(self, candidate):
        neighbors = []
        for i in range(len(candidate)-1):
            c = candidate.copy()
            c[i] += c[i+1]
            c[i+1] = c[i] - c[i+1]
            c[i] = c[i] - c[i+1]
            neighbors.append(c)

        return neighbors

class RandomSwapHillclimbing(HillClimbing):
    def generate_neighbors(self, candidate):
        neighbors = []
        for i in range(len(candidate)):
            c = candidate.copy()
            r = random.randint(0, len(candidate)-1)
            while r == i:
                r = random.randint(0, len(candidate)-1)
            c[i] += c[r]
            c[r] = c[i] - c[r]
            c[i] = c[i] - c[r]
            neighbors.append(c)

        return neighbors

class SegmentReversalHillclimbing(HillClimbing):
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

            neighbors.append(c)

        return neighbors