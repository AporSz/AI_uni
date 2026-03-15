from hw1.part2.solvers.entropy import Entropy
from hw1.part2.utils.data_loader import DataLoader

data_loader = DataLoader('data/PlayTennis.csv')
data = data_loader.get_data()
entropy_calculator = Entropy(data)
a = entropy_calculator.get_attributes()
print(entropy_calculator.make_tree())