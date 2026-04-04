We take an individual (a particle).

We look at his surrounding (neighborhood).

We find the "alpha"  (the individual with the best fitness value) and find the vector towards him from the individual.

We calculate the [[Community Influence]] on the individual and add it to the previous result.

We finally consider [[Short Term Memory]] and add the result to that.

Parameters:
- alpha: how much is the community influencing the individual
- beta: how much is the attraction towards the "alpha" individual
- gamma: how much the [[Short Term Memory]] influences the individual

