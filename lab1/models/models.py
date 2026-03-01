class KnapsackProblem:
    def __init__(self, weights, values, capacity, penalty_ratio = 0.5):
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
        value = 0
        weight = 0
        for i in range(len(candidate)):
            if candidate[i] == 1:
                weight += self._weights[i]
                value += self._values[i]

        if weight > self._capacity:
            value -= (weight - self._capacity) * self._penalty_ratio
            return max(value, 0)

        return value