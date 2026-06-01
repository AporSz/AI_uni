import struct
import numpy as np
from fontTools.misc.bezierTools import epsilon


# https://ajcr.net/fast-inverse-square-root-python/
def quack3_np(number):
    threehalfs = 1.5
    x2 = number * 0.5
    y = np.float32(number)

    i = y.view(np.int32)
    i = np.int32(0x5f3759df) - np.int32(i >> 1)
    y = i.view(np.float32)

    y = y * (threehalfs - (x2 * y * y))
    return float(y)

# https://www.geeksforgeeks.org/dsa/fast-inverse-square-root/
def quack3_struct(number):
    threehalfs = 1.5
    x2 = number * 0.5
    y = number

    # evil floating point bit level hacking
    i = struct.unpack('I', struct.pack('f', y))[0]
    i = 0x5f3759df - (i >> 1)
    y = struct.unpack('f', struct.pack('I', i))[0]

    # 1st iteration
    y = y * (threehalfs - (x2 * y * y))

    # 2nd iteration, this can be removed
    # y = y * (threehalfs - (x2 * y * y))
    result_bits = struct.unpack('I', struct.pack('f', y))[0]
    size = struct.calcsize('I')

    if result_bits < 0 or result_bits >= (1 << (size * 8)):
        raise ValueError('result_bits out of range')

    return struct.unpack('f', struct.pack('I', result_bits))[0]

print(quack3_np(2))
print(quack3_struct(2))
print(1/np.sqrt(2))

p = [-1, 0, 1]

def derivative(poly):
    d = [0] * len(poly)

    for i in range(len(poly)):
        d[i] = i * poly[i]

    return d[1:]

def polynomial_value(poly, x):
    value = 0

    for i in range(len(poly)):
        value += poly[i] * (x ** i)

    return value

def newtons_method(poly, x, iterations, epsilon):
    if iterations < 0:
        raise ValueError('iterations out of range')

    if iterations == 0:
        return x

    if abs(polynomial_value(poly, x)) < epsilon:
        return x

    denominator = polynomial_value(derivative(poly), x)
    if denominator == 0:
        raise ValueError('Derivative is 0, the method fails')

    x1 = x - polynomial_value(poly, x) / denominator
    return newtons_method(poly, x1, iterations - 1, epsilon)

def start_newton(poly, a, b, iterations, epsilon):
    if iterations < 0:
        raise ValueError('iterations out of range')

    if epsilon <= 0:
        raise ValueError('epsilon out of range')

    d = derivative(poly)
    x = np.linspace(a, b, 100)
    for value in x:
        if polynomial_value(d, value) < 0:
            raise ValueError('Polynomial decreasing')

    dd = derivative(d)
    for value in x:
        if polynomial_value(dd, value) < 0:
            raise ValueError('Polynomial not convex')

    pa = polynomial_value(poly, a)
    pb = polynomial_value(poly, b)

    if pa * pb > 0:
        raise ValueError("The interval [a, b] is not guaranteed to contain a root. P(a) and P(b) must have opposite signs.")

    return newtons_method(poly, b, iterations, epsilon)

print(newtons_method([-1, 0, 1], 0.5, 10, 0.001))
print(polynomial_value(p, 1))

def nth_root(x, n):
    poly = np.zeros(n + 1)

    poly[0] = -x
    poly[-1] = 1

    return start_newton(poly, 0, x, 100, 0.00001)

print(nth_root(17, 9))