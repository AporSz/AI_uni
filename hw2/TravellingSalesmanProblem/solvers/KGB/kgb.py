import random

from hw2.TravellingSalesmanProblem.solvers.basesolver import BaseSolver, validate


class Tree:
    def __init__(self, value, level, nr_of_children, solver, health = 5, children = None):
        self._value = value
        self._level = level
        self._children = children
        self._nr_of_children = nr_of_children
        self._solver = solver
        self._health = health

    def decrease_health(self, number):
        self._health = self._health - number
        if  self._health <= 0:
            return False
        
        return True

    def regenerate(self, number, height):
        if self._level == height:
            self._value = self._solver.climb(self._value)
            return self._value

        # if self._children is None:
        #     return

        if number > len(self._children):
            raise ValueError("You can't remove more children than the number of children")

        self._children.sort(key=lambda x: self._solver.fitness(x._value), reverse=True)

        # m = 100000 # for not directly increasing values
        m = self._solver.fitness(self._value)

        # for i in range(number):
        #     child = Tree(None, self._level + 1, self._nr_of_children, self._solver)
        #     v = child.generate_tree(height)
        #     f = self._solver.fitness(v)
        #     if f < m:
        #         m = f
        #         self._value = v
        #     self._children[i] = child

        # for i in range(number, self._nr_of_children):
        #     v = self._children[i].regenerate(number, height)
        #     f = self._solver.fitness(v)
        #     if f < m:
        #         m = f
        #         self._value = v

        for i in range(self._nr_of_children):
            if i < number:
                if self._children[i].decrease_health(1):
                    v = self._children[i].regenerate(number, height)
                else:
                    child = Tree(None, self._level + 1, self._nr_of_children, self._solver, (height - (self._level + 1)) * 5)
                    v = child.generate_tree(height)
                    self._children[i] = child
            else:
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
                child = Tree(None, self._level + 1, self._nr_of_children, self._solver, (height - (self._level + 1)) * 5)
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

class KGBSolver(BaseSolver):
    def __init__(self, problem, iterations = 100, tree_height = 5, nr_of_children = 5):
        BaseSolver.__init__(self, problem)
        self._iterations = iterations
        self._tree_height = tree_height
        self._nr_of_children = nr_of_children
        self._tabu = set()

    def tabu(self, candidate):
        t = tuple(candidate)

        if t in self._tabu:
            return False

        self._tabu.add(t)
        return True

    def solve(self):
        tree = Tree(None, 1, nr_of_children = self._nr_of_children, solver = self)
        tree.generate_tree(self._tree_height)
        
        best = 100000
        solution = None

        for i in range(self._iterations):
            ratio = 0.25
            # ratio = 1 - i / self._iterations
            v = tree.regenerate(int(self._nr_of_children * ratio), self._tree_height)
            f = self.fitness(v)
            if f < best:
                best = f
                solution = v
            print(self.fitness(v))

        
        print("===================")
        print("Valid: " + str(validate(solution)))
        print(best)
        print(solution)
        with (open("../../crazy.txt", "a") as file):
        # with (open("crazy.txt", "a") as file):
            file.write(str(best))
            file.write(str("\n"))
            file.write(str(solution))
            file.write(str("\n"))
            file.write("=================================================================================\n")

    def climb(self, candidate):
        neighbors = self.neighborhood(candidate)

        m = 100000
        v = candidate

        for n in neighbors:
            f = self.fitness(n)
            if f < m :
                m = f
                v = n

        return v
    
    # all 52 x 52 neighbors
    # def neighborhood(self, candidate):
    #     neighbors = []
    #     for i in range(len(candidate)):
    #         for j in range(i + 1, len(candidate)):
    #             c = candidate.copy()
    #             if i != j:
    #                 aux = c[i]
    #                 c[i] = c[j]
    #                 c[j] = aux

    #             if self.tabu(c):
    #                 neighbors.append(c)
    #     return neighbors

    # swapping random elements
    # def neighborhood(self, candidate):
    #     neighbors = []
    #     for i in range(len(candidate)):
    #         c = candidate.copy()
    #         r = random.randint(0, len(candidate)-1)
    #         while r == i:
    #             r = random.randint(0, len(candidate)-1)
    #         c[i] += c[r]
    #         c[r] = c[i] - c[r]
    #         c[i] = c[i] - c[r]
    #         if self.tabu(c):
    #             neighbors.append(c)

    #     return neighbors

    # reversing random segments
    def neighborhood(self, candidate):
        neighbors = []
        for i in range(len(candidate)):
            c = candidate.copy()
            r = random.randint(0, len(candidate) - 1)
            while r == i:
                r = random.randint(0, len(candidate) - 1)

            a = min(i, r)
            b = max(i, r)
            segment = c[a:b]
            segment.reverse()
            c = c[:a] + segment + c[b:]

            # if self.tabu(c):
            #     neighbors.append(c)

            neighbors.append(c)

        return neighbors