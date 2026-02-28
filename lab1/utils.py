def get_nr_of_candidates():
    try:
        candidates = int(input('How many candidates would you like? '))
        if candidates < 1:
            print('Please enter a positive integer larger than 0')
            return get_nr_of_candidates()
        return candidates
    except ValueError as e:
        print(e)
        print('Please enter a NUMBER larger than 0')
        return get_nr_of_candidates()

def get_nr_of_problems():
    try:
        nr_of_problems = int(input('How many problems would you like? '))
        if nr_of_problems < 1:
            print('Please enter a positive integer larger than 0')
            return get_nr_of_problems()
        if nr_of_problems > 9999:
            print('Please enter a number smaller than 10000')
            return get_nr_of_problems()
        return nr_of_problems
    except ValueError as e:
        print(e)
        print('Please enter a NUMBER larger than 0 but smaller than 10000')
        return get_nr_of_problems()

def calculate_value(candidate, size, weights=None, prices=None, capacity=None, problem=None):
    if problem is not None:
        weights, prices, capacity = problem

    current_capacity = 0
    current_value = 0
    for i in range(size):
        if candidate[i] == 1:
            current_capacity += weights[i]
            current_value += prices[i]
    if current_capacity > capacity:
        return 0
    return current_value

# print(calculate_value([1],1,problem=[[1],[1],1]))