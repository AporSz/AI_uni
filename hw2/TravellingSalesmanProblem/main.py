import matplotlib.pyplot as plt

from hw2.TravellingSalesmanProblem.plotter import plot_all
from hw2.TravellingSalesmanProblem.solvers.KGB.kgb import Tree, KGBSolver
from hw2.TravellingSalesmanProblem.solvers.evolutionary.evolutionary import *
from hw2.TravellingSalesmanProblem.solvers.hillclimbing.simple_hillclimbing import SimpleNeighborSwapHillclimbing, \
    RandomSwapHillclimbing, SegmentReversalHillclimbing
from hw2.TravellingSalesmanProblem.solvers.hillclimbing.simulated_annealing import SimulatedAnnealing
from hw2.TravellingSalesmanProblem.solvers.hillclimbing.tabusearch import TabuSearchHillClimbing
from hw2.TravellingSalesmanProblem.utils.data_loader import DataLoader

ITERATIONS = 1000

dataloader = DataLoader('data/berlin52.tsp')
# dataloader = DataLoader('hw2/TravellingSalesmanProblem/data/berlin52.tsp')

data = dataloader.get_data()

plot_all(data, ITERATIONS)