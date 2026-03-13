import numpy as np

class Entropy:
    def __init__(self, data):
        self._data = data

    def calculate_entropy(self,) -> float:
        pass

    def calculate_probability(self, attribute, value) -> float:
        n = len(self._data)
        i = 0
        for entry in self._data:
            if entry[attribute] == value:
                i += 1

        return i/n