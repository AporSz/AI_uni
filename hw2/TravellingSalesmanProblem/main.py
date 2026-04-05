import matplotlib.pyplot as plt

from hw2.TravellingSalesmanProblem.solvers.hillclimbing.simple_hillclimbing import SimpleNeighborSwapHillclimbing, \
    RandomSwapHillclimbing, SegmentReversalHillclimbing
from hw2.TravellingSalesmanProblem.utils.data_loader import DataLoader

ITERATIONS = 50

dataloader = DataLoader('data/berlin52.tsp')
data = dataloader.get_data()

# print(data)

solver1 = SimpleNeighborSwapHillclimbing(problem = data, iterations = ITERATIONS, climbers = 25)
solver2 = RandomSwapHillclimbing(problem = data, iterations = ITERATIONS * 2, climbers = 25)
solver3 = SegmentReversalHillclimbing(problem = data, iterations = ITERATIONS * 3, climbers = 25)

results = solver1.solve()

for i in results:
    plt.plot(results[i])

plt.show()

results = solver2.solve()

for i in results:
    plt.plot(results[i])

plt.show()

results = solver3.solve()

for i in results:
    plt.plot(results[i])

plt.show()