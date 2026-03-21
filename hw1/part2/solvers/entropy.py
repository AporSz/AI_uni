import numpy as np

class Entropy:
    def __init__(self, data):
        self._data = data
        self._attributes = {}
        self._attributes = self.get_attributes()

    def get_attributes(self):
        if len(self._attributes) != 0:
            return self._attributes

        if len(self._data) == 0:
            return None

        attributes = {}
        for key, value in self._data[0].items():
            attributes[key] = {}

        for entry in self._data:
            for key, value in entry.items():
                if value not in attributes[key]:
                    attributes[key][value] = 1
                else:
                    attributes[key][value] += 1

        return attributes

    def calculate_entropy(self, attribute):
        if attribute not in self._attributes:
            raise ValueError("Attribute " + attribute + " is not present in the data")
        entropy = 0
        n = len(self._data)

        for key, value in self._attributes[attribute].items():
            probability = value / n
            entropy -= probability * np.log2(probability)

        return entropy

    def calculate_information_gain(self, attribute):
        if attribute not in self._attributes:
            raise ValueError("Attribute " + attribute + " is not present in the data")

        gain = self.calculate_entropy('Play Tennis')
        n = len(self._data)

        for value, count in self._attributes[attribute].items():
            mini_data = []
            for entry in self._data:
                if entry[attribute] == value:
                    mini_data.append(entry)

            mini_calculator = Entropy(mini_data)
            mini_entropy = mini_calculator.calculate_entropy('Play Tennis')

            gain = gain - ((count / n) * mini_entropy)

        return gain

    def make_tree(self):
        from hw1.part2.datastructures.decision_tree import Node

        max_information_gain, best_attribute = 0, None
        for attribute in self._attributes:
            gain = self.calculate_information_gain(attribute)
            if gain > max_information_gain and attribute != 'Play Tennis':
                max_information_gain = gain
                best_attribute = attribute

        if best_attribute is None:
            return Node(f"Play Tennis: {self._data[0]['Play Tennis']}", {})

        tree_data = {}
        for value in self._attributes[best_attribute]:
            tree_data[value] = []

        for entry in self._data:
            aux = entry[best_attribute]
            del entry[best_attribute]
            tree_data[aux].append(entry)

        root = Node(best_attribute, tree_data)

        return root


    def __str__(self):
        acc = ""
        for a in self._attributes:
            acc += str(a) + " "
        acc += "\n"
        for entry in self._data:
            for key, value in entry.items():
                acc += str(value) + " "
            acc += "\n"
        return acc