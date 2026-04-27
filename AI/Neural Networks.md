
Made of neurons that have:
- Inputs: x0, x1, ... , xn
- Weights: w0, w1,  ... , wn
	- initialized randomly
- [[Activation Function]]: f
- output: 
	- o = f(a)
	- a = w0x0 + 21x1 + ... + wnxn

- activation degree: the value of the activation function

- [[Error]](o) = 1/2 (o - y) ^2
	- where y is the expected value

Just like in [[Machine Learning]] we have the feed forward of information then the back propagation of errors (which means the recalibration of weights of the neuron)

If have the sigmoid activation function as our activation function:
	f'(a) = f(a) (1 - f(a)) -> Err(w0, w1) = 1/2 (1/1 + e^(-(w0x0 + w1x1)))
We can find the partial derivative of the Error function with respect to the weights


w0'' = w0' - mew * (the partial derivative of the error with respect to w0)
- same with w1
- mew = learning rate