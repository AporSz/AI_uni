import numpy as np

class Entropy:
    def __init__(self, data):
        self._data = data

    def calculate_entropy(self, attribute) -> float:
        visited = set()
        entropy = 0
        for entry in self._data:
            value = entry[attribute]
            if value not in visited:
                visited.add(value)
                probability = self.calculate_probability(attribute, value)
                entropy -= probability * np.log2(probability)
        return entropy

    def calculate_probability(self, attribute, value) -> float:
        n = len(self._data)
        i = 0
        for entry in self._data:
            if entry[attribute] == value:
                i += 1

        return i/n
    
if __name__ == "__main__":
    data_loader = DataLoader('hw1/part2/data/PlayTennis.csv')
    data = data_loader.get_data()
    entropy_calculator = Entropy(data)
    print(entropy_calculator.calculate_entropy('Play Tennis'))