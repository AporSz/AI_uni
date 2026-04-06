
Phases:
- Training
- Testing

First machine to do it: [[Mark I Perceptron]]

AND with machine learning:
- it's binary classification
- training dataset: AND truth table
- one line from the dataset is a training instance
- a column from the dataset is a feature attribute
- if you plot the truth table you can see it's a linearly separable input: ax+by = 0 (we ignore c (or bias) for now)

 We start with n inputs. All inputs have weights. We initialize the input weights with random values.

Feed Forward of Information:
- input is processed and set towards the next neuron (it's tree structure and we start from the leaves).

Back Propagation of Errors:
- you change the trust weight of each input to correct the [[Error]]s