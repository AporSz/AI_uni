import matplotlib.pyplot as plt

from hw2.TravellingSalesmanProblem.solvers.hillclimbing.simple_hillclimbing import SimpleNeighborSwapHillclimbing, \
    RandomSwapHillclimbing, SegmentReversalHillclimbing
from hw2.TravellingSalesmanProblem.solvers.hillclimbing.simulated_annealing import SimulatedAnnealing
from hw2.TravellingSalesmanProblem.solvers.hillclimbing.tabusearch import TabuSearchHillClimbing
from hw2.TravellingSalesmanProblem.utils.data_loader import DataLoader

ITERATIONS = 1000

dataloader = DataLoader('data/berlin52.tsp')
data = dataloader.get_data()

# print(data)

# solver1 = SimpleNeighborSwapHillclimbing(problem = data, iterations = ITERATIONS, climbers = 25)
# solver2 = RandomSwapHillclimbing(problem = data, iterations = ITERATIONS * 5, climbers = 25)
# solver3 = SegmentReversalHillclimbing(problem = data, iterations = ITERATIONS * 5, climbers = 25)

solver = SimulatedAnnealing(problem = data, iterations = ITERATIONS, climbers = 25)

# results = solver1.solve()
#
# for i in results:
#     plt.plot(results[i])
#
# plt.show()
#
# results = solver2.solve()
#
# for i in results:
#     plt.plot(results[i])
#
# plt.show()
#
# results = solver3.solve()
#
# for i in results:
#     plt.plot(results[i])
#
# plt.show()

results = solver.solve()

m = 30000
for i in results:
    mres = min(*results[i])
    if mres < m:
        m = mres
    plt.plot(results[i])

plt.show()

print(m)