
Survival of the fittest. (Charles Darwin)

Genetic recombination -> Mutation -> Survival of the fittest

Genetic recombination:
- we take a random sample from the population and select the best from it (twice) and those two are the parents
- we use one parent for indexes and the other one for information
Mutation:
- swap of elements in a permutation
- this effects everyone in the population
Survival of the fittest:
- we only keep the first half (better half) of the population

for i in range(n):
	rand = random
	if rand > 0.5:
		child{i} = parent_1{i}
	else:
		child{i} = parent_2{i}