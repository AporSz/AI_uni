import numpy as np

from hw1.part2.utils.fuzzy_utils import FuzzyUtils


class FuzzyEntropy:
    def __init__(self, data, weights):
        self._data = data
        self._weights = weights
        self.fu = FuzzyUtils()
        self._attributes = {}
        self._attributes = self.get_attributes()

    def get_attributes(self):
        if len(self._attributes) != 0:
            return self._attributes

        if len(self._data) == 0:
            return None

        attributes = {}
        # for key, value in self._data[0].items():
        #     attributes[key] = []

        for index, entry in enumerate(self._data):
            for key, value in entry.items():
                membership = self.fu.attribute_membership(key, value)
                if key not in attributes:
                    if entry['target'] == 0:
                        attributes[key] = {
                            0: membership * self._weights[index],
                            1: np.zeros(len(membership))
                        }
                    else:
                        attributes[key] = {
                            1: membership * self._weights[index],
                            0: np.zeros(len(membership))
                        }
                else:
                    for i in range(len(membership)):
                        if entry['target'] == 0:
                            attributes[key][0][i] += membership[i] * self._weights[index]
                        else:
                            attributes[key][1][i] += membership[i] * self._weights[index]

        return attributes

    def calculate_entropy(self, attribute):
        if attribute not in self._attributes:
            raise ValueError("Attribute " + attribute + " is not present in the data")
        entropy = 0

        # for key, value in self._attributes[attribute].items():
        #     n = value[0] + value[1]
        #     for i, entry in enumerate(value):
        #         probability = entry / n[i]
        #         entropy -= probability * np.log2(probability)

        n = self._attributes[attribute][0] + self._attributes[attribute][1]
        weight = n.sum()
        for i, entry in enumerate(self._attributes[attribute][0]):
            probability = 0
            if n[i] != 0:
                probability = entry / n[i]
            if probability > 0:
                entropy -= probability * np.log2(probability) * (n[i] / weight)

        for i, entry in enumerate(self._attributes[attribute][1]):
            probability = 0
            if n[i] != 0:
                probability = entry / n[i]
            if probability > 0:
                entropy -= probability * np.log2(probability) * (n[i] / weight)

        return entropy

    def base_entropy(self):
        t0 = sum(self._weights[i] for i, e in enumerate(self._data) if e['target'] == 0)
        t1 = sum(self._weights[i] for i, e in enumerate(self._data) if e['target'] == 1)
        total = t0 + t1
        entropy = 0
        for count in [t0, t1]:
            p = count / total
            if p > 0:
                entropy -= p * np.log2(p)
        return entropy

    def calculate_information_gain(self, attribute):
        if attribute not in self._attributes:
            raise ValueError("Attribute " + attribute + " is not present in the data")

        return self.base_entropy() - self.calculate_entropy(attribute)

    def make_tree(self):
        from hw1.part2.datastructures.fuzzy_tree import FuzzyNode

        max_information_gain, best_attribute = 0, None
        for attribute in self._attributes:
            gain = self.calculate_information_gain(attribute)
            if gain > max_information_gain and attribute != 'target':
                max_information_gain = gain
                best_attribute = attribute

        if best_attribute is None:
            return FuzzyNode(f"Disease: {self._data[0]['target']}", {})

        tree_data = {}
        for value in self._attributes[best_attribute]:
            tree_data[value] = []

        for entry in self._data:
            aux = entry[best_attribute]
            del entry[best_attribute]
            tree_data[aux].append(entry)

        root = FuzzyNode(best_attribute, tree_data)

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