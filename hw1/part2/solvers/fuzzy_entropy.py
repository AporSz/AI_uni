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

        # Calculate weighted class sums for the current node
        t0 = sum(self._weights[i] for i, e in enumerate(self._data) if e['target'] == 0)
        t1 = sum(self._weights[i] for i, e in enumerate(self._data) if e['target'] == 1)

        # Determine the dominant target class
        prediction = 0 if t0 >= t1 else 1

        # Check stopping criteria
        # 1. Pure node
        if t0 == 0 or t1 == 0:
            return FuzzyNode(f"Disease: {prediction}")

        # 2. No attributes left to split on besides 'target'
        available_attributes = [k for k in self._attributes if k != 'target']
        if len(available_attributes) == 0:
            return FuzzyNode(f"Disease: {prediction}")

        # 3. Choose the best attribute based on information gain
        max_information_gain, best_attribute = 0, None
        for attribute in available_attributes:
            gain = self.calculate_information_gain(attribute)
            if gain > max_information_gain:
                max_information_gain = gain
                best_attribute = attribute

        # If no positive information gain can be achieved, return a leaf node
        if best_attribute is None or max_information_gain <= 1e-9:
            return FuzzyNode(f"Disease: {prediction}")

        # 4. Construct children nodes recursively by branching on linguistic terms
        terms = list(self.fu.config[best_attribute].keys())
        child_nodes = {}

        for term in terms:
            new_data = []
            new_weights = []
            m_func = self.fu.config[best_attribute][term]

            for i, entry in enumerate(self._data):
                m_value = m_func(entry[best_attribute])
                w_new = self._weights[i] * m_value

                # Only propagate instances that have a significant membership degree in this branch
                if w_new > 1e-5:
                    entry_copy = entry.copy()
                    del entry_copy[best_attribute]
                    new_data.append(entry_copy)
                    new_weights.append(w_new)

            if len(new_data) > 0:
                child_solver = FuzzyEntropy(new_data, np.array(new_weights))
                child_nodes[term] = child_solver.make_tree()
            else:
                # Default leaf node if no data falls into this branch
                child_nodes[term] = FuzzyNode(f"Disease: {prediction}")

        return FuzzyNode(best_attribute, child_nodes)


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