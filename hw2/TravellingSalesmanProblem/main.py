import matplotlib.pyplot as plt

from hw2.TravellingSalesmanProblem.solvers.hillclimbing import HillClimbing
from hw2.TravellingSalesmanProblem.utils.data_loader import DataLoader

ITERATIONS = 50

dataloader = DataLoader('data/berlin52.tsp')
data = dataloader.get_data()

# print(data)

solver1 = HillClimbing(problem = data, iterations = ITERATIONS, climbers = 25)

results = solver1.solve()

for i in results:
    plt.plot(results[i])

plt.show()