import matplotlib

from hw2.TravellingSalesmanProblem.plotter import plot_all
from hw2.TravellingSalesmanProblem.utils.data_loader import DataLoader

matplotlib.use('TkAgg')

ITERATIONS = 100

dataloader = DataLoader('data/berlin52.tsp')
# dataloader = DataLoader('hw2/TravellingSalesmanProblem/data/berlin52.tsp')

data = dataloader.get_data()

plot_all(data, ITERATIONS)