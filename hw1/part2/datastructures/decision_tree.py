from hw1.part2.solvers.entropy import Entropy

class Node:
    def __init__(self, value, data, children=None):
        self._value = value
        self._data = data

        if children is None:
            self._children = []
        else:
            self._children = children

        self.process_data()


    def add_child(self, node):
        self._children.append(node)

    def get_children(self):
        return self._children

    def process_data(self):
        if isinstance(self._data, dict):
            for value in self._data:
                self.add_child(Node(value, self._data[value]))
        else:
            calculator = Entropy(self._data)
            self.add_child(calculator.make_tree())

    def __str__(self, level=0):
        # Create indentation based on the current depth (level)
        indent = "    " * level

        # Format the current node's value
        acc = f"{indent}└── {self._value}\n"

        # Recursively call __str__ on children, increasing the depth level
        for child in self._children:
            acc += child.__str__(level + 1)

        return acc