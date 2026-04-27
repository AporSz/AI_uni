from abc import abstractmethod
import random
import numpy as np

from hw2.TravellingSalesmanProblem.solvers.basesolver import BaseSolver, validate


class EvolutionarySolver(BaseSolver):
    def __init__(self, problem, iterations = 100, population_size = 100, mutation_rate = 1, sample_size = 25):
        super().__init__(problem = problem)
        self._population_size = population_size
        self._mutation_rate = mutation_rate
        self._iterations = iterations
        self._sample_size = sample_size
        self._best_values = {}
        self._top = 25

    def generate_population(self):
        population = []

        for i in range(self._population_size):
            population.append(self.generate_random())

        return population
    
    def mutate(self, individual):
        r = random.random()

        if r < self._mutation_rate:
            a = random.randint(0, len(individual) - 1)
            b = random.randint(0, len(individual) - 1)
            while a == b:
                b = random.randint(0, len(individual) - 1)

            individual[a] += individual[b]
            individual[b] = individual[a] - individual[b]
            individual[a] = individual[a] - individual[b]
    
    def mutate_population(self, population):
        for i in range(len(population)):
            self.mutate(population[i])

    def solve(self):
        population = self.generate_population()

        for j in range(self._top):
            self._best_values[j] = []

        for i in range(self._iterations):
            self.cycle_population(population)
            for j in range(self._top):
                self._best_values[j].append(self.fitness(population[j]))
                # validate(population[j])

        return self._best_values

    def reproduce(self, parent1, parent2):
        if len(parent1) != len(parent2):
            raise ValueError("The parents must have the same length")
        
        child = np.zeros(len(parent1)).tolist()
        for i in range(len(child)):
            child[i] = parent1[parent2[i]-1]

        return child
    
    def survival_of_the_fittest(self, population):
        population.sort(key = self.fitness)

        for i in range(self._population_size):
            population.pop(len(population) - 1)
    
    def cycle_population(self, population):
        self.double_population(population)

        self.mutate_population(population)

        self.survival_of_the_fittest(population)

    def double_population(self, population):
        n = len(population)
        for i in range(n):
            p1, p2 = self.find_parents(population[:n])
            population.append(self.reproduce(p1, p2))

    def find_parents(self, population):
        if self._sample_size > self._population_size:
            raise ValueError("The sample must be smaller than the population size!")
        
        sample = set()
        
        best1 = None
        best2 = None
        min1 = 1000000
        min2 = 1000000

        for i in range(self._sample_size):
            r = random.randint(0, len(population) - 1)
            while r in sample:
                r = random.randint(0, len(population) - 1)
            sample.add(r)

            m = self.fitness(population[r])
            if m < min1:
                min2 = min1
                best2 = best1
                min1 = m
                best1 = population[r]
            elif m < min2:
                min2 = m
                best2 = population[r]

        return best1, best2
    
class EvolutionaryVariantRandom(EvolutionarySolver):
    def find_parent(self, population):
        a = random.randint(0, len(population) - 1)
        b = random.randint(0, len(population) - 1)

        return population[a], population[b]
    
class EvolutionaryVariant(EvolutionarySolver):
    def reproduce(self, parent1, parent2):
        if len(parent1) != len(parent2):
            raise ValueError("The parents must have the same length")
        
        child1 = np.zeros(len(parent1)).tolist()
        for i in range(len(child1)):
            child1[i] = parent1[parent2[i]-1]

        child2 = np.zeros(len(parent1)).tolist()
        for i in range(len(child2)):
            child2[i] = parent2[parent1[i]-1]

        return child1, child2
    
    def double_population(self, population):
        n = len(population)
        for i in range(n//2):
            p1, p2 = self.find_parents(population[:n])
            ch1, ch2 = self.reproduce(p1, p2)
            population.append(ch1)
            population.append(ch2)

class ChernobylKids(EvolutionarySolver):
    # def mutate_population(self, population):
    #     for i in range(len(population)//2, len(population)):
    #         self.mutate(population[i])

    def reproduce(self, parent1, parent2):
        if len(parent1) != len(parent2):
            raise ValueError("The parents must have the same length")
        
        child = np.zeros(len(parent1)).tolist()
        
        a = random.randint(0, len(parent1) - 1)
        b = random.randint(0, len(parent1) - 1)
        while a == b:
            b = random.randint(0, len(parent1) - 1)

        if a > b:
            a = a + b
            b = a - b
            a = a - b

        for i in range(a, b):
            child[i - a] = parent1[i]

        parent2_genes = []

        for i in range(len(parent2)):
            if parent2[i] not in child:
                parent2_genes.append(parent2[i])

        aux = len(child) - len(parent2_genes)
        for i in range(len(parent2_genes)):
            child[aux + i] = parent2_genes[i]

        return child