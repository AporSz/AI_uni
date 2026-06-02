import numpy as np

from hw1.part2.solvers.entropy import Entropy
from hw1.part2.solvers.fuzzy_entropy import FuzzyEntropy
from hw1.part2.utils.data_loader import DataLoader
from hw1.part2.utils.fuzzy_utils import FuzzyUtils


def play_tennis():
    data_loader = DataLoader('data/PlayTennis.csv')
    data = data_loader.get_data_play_tennis()
    print(data)
    entropy_calculator = Entropy(data)
    # print(entropy_calculator.get_attributes())

    print(entropy_calculator.make_tree())

def heart_disease():
    data_loader = DataLoader('data/Heart_disease_cleveland_new.csv')
    data = data_loader.get_data_heart_disease()

    weights = np.ones(len(data))

    calc = FuzzyEntropy(data, weights)
    # print(data)
    print(calc.calculate_information_gain("sex"))

heart_disease()

# fu = FuzzyUtils()
# print(fu.attribute_membership("age", 40))