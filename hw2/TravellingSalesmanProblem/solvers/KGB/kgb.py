from hw2.TravellingSalesmanProblem.solvers.basesolver import BaseSolver


class Tree:
    def __init__(self, value, level, nr_of_children, solver, children = None):
        self._value = value
        self._level = level
        self._children = children
        self._nr_of_children = nr_of_children
        self._solver = solver

    def regenerate(self, number, height):
        if self._level == height:
            self._value = self._solver.climb(self._value)
            return self._value
            self._value = self._solver.generate_random()
            return self._value

        # if self._children is None:
        #     return

        if number > len(self._children):
            raise ValueError("You can't remove more children than the number of children")

        self._children.sort(key=lambda x: self._solver.fitness(x._value), reverse=True)

        m = 100000

        for i in range(number):
            child = Tree(None, self._level + 1, self._nr_of_children, self._solver)
            v = child.generate_tree(height)
            f = self._solver.fitness(v)
            if f < m:
                m = f
                self._value = v
            self._children[i] = child

        for i in range(number, self._nr_of_children):
            v = self._children[i].regenerate(number, height)
            f = self._solver.fitness(v)
            if f < m:
                m = f
                self._value = v

        return self._value


    def generate_tree(self, height):
        #simulated annealing goes hard
        if self._level == height:
            self._value = self._solver.generate_random()
            return self._value
        else:
            self._children = []
            m = 100000
            for i in range(self._nr_of_children):
                child = Tree(None, self._level + 1, self._nr_of_children, self._solver)
                v = child.generate_tree(height)
                f = self._solver.fitness(v)
                if f < m:
                    m = f
                    self._value = v
                self._children.append(child)

            return self._value

    def __str__(self):
        # string = str(self._value)
        string = str(self._solver.fitness(self._value)) + "\n"
        if self._children is None:
            return string
        for child in self._children:
            for j in range(self._level):
                string += " "
            if child is not None:
                string += "|__" + str(child)
            else:
                string += "|__" + str(child)

        return string


def neighborhood(candidate):
    neighbors = []
    for i in range(len(candidate)):
        for j in range(len(candidate)):
            c = candidate.copy()
            if i != j:
                aux = c[i]
                c[i] = c[j]
                c[j] = aux

            neighbors.append(c)
    return neighbors

class KGBSolver(BaseSolver):
    def __init__(self, problem, iterations = 100, tree_height = 5, nr_of_children = 5):
        BaseSolver.__init__(self, problem)
        self._iterations = iterations
        self._tree_height = tree_height
        self._nr_of_children = nr_of_children

    def solve(self):
        tree = Tree(None, 1, nr_of_children = self._nr_of_children, solver = self)
        tree.generate_tree(self._tree_height)

        for i in range(self._iterations):
            v = tree.regenerate(self._nr_of_children//2, self._tree_height)
            print(self.fitness(v))

    def climb(self, candidate):
        neighbors = neighborhood(candidate)

        m = 100000
        v = candidate

        for n in neighbors:
            f = self.fitness(n)
            if f < m:
                m = f
                v = n

        return v