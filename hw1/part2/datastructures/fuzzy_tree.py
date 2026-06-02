class FuzzyNode:
    def __init__(self, value, children=None):
        self._value = value
        # self._children maps branch labels (e.g. linguistic terms) to child FuzzyNodes
        self._children = children if children is not None else {}

    def get_children(self):
        return self._children

    def __str__(self, level=0):
        # Create indentation based on the current depth (level)
        indent = "    " * level

        # Format the current node's value
        acc = f"{indent}└── {self._value}\n"

        # Recursively call __str__ on children, showing the branch label
        for branch, child in self._children.items():
            acc += f"{indent}    ({branch})\n"
            acc += child.__str__(level + 2)

        return acc