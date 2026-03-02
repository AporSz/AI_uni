class KnapsackProblem:
    def __init__(self, weights, values, capacity, penalty_ratio = 5):
        if len(weights) != len(values):
            raise ValueError('Weights and values must have the same length!')
        if capacity <= 0:
            raise ValueError('Capacity must be positive!')
        self._weights = weights
        self._values = values
        self._capacity = capacity
        self._penalty_ratio = penalty_ratio

    def capacity(self):
        return self._capacity

    def penalty_ratio(self):
        return self._penalty_ratio

    def evaluate(self, candidate):
        if len(candidate) != len(self._values):
            raise ValueError('Candidate must have the same length!')
        value = self.get_value(candidate)
        weight = self.get_weight(candidate)

        if weight > self._capacity:
            value -= (weight - self._capacity) * self._penalty_ratio
            return max(value, 0)

        return value

    def __len__(self):
        return len(self._weights)

    def __str__(self):
        return f"Weights: {self._weights}, Values: {self._values}, Capacity: {self._capacity}"

    def is_feasible(self, candidate):
        if len(candidate) != len(self._values):
            raise ValueError('Candidate must have the same length!')
        if self.capacity() <= self.get_weight(candidate):
            return False

        return True

    def get_value(self, candidate):
        if len(candidate) != len(self._values):
            raise ValueError('Candidate must have the same length!')
        value = 0
        for i in range(len(candidate)):
            if candidate[i] == 1:
                value += self._values[i]
        return value

    def get_weight(self, candidate):
        if len(candidate) != len(self._values):
            raise ValueError('Candidate must have the same length!')
        weight = 0
        for i in range(len(candidate)):
            if candidate[i] == 1:
                weight += self._weights[i]

        return weight