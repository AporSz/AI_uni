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