You can represent a problem with the following:
	P = {Vi belongs to DVi}

Most basic way to solve it is brute force.

Brute force:

for a0 in Dv0:
	for a1 in Dv1:
		...
		...
			for an in Dvn:
				candidate(a0, a1, ..., an) <-- Position

Can be optimized with [[Divide et Impera]] or Dynamic Programming or Greedy.