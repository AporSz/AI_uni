class Node:
    def __init__(self, data, children=None):
        self._data = data
        self._children = children

    def add_child(self, node):
        self._children.append(node)

    def get_children(self):
        return self._children