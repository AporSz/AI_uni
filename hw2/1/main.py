import numpy as np

# polynomial representation: a0 + a1 * x + a2 * x^2 + ... an * x^n
p1 = np.array([9, -10, 7, 6])
p2 = np.array([-5, 4, 0, -2])

test = np.array([1, 2, 3, 4])

p3 = np.array([-7, 1, 0, 1])
p4 = np.array([9, 1, 1, 0])

def bruteforce(poly1, poly2):
    result = np.zeros(len(poly1) + len(poly2) - 1)

    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] += poly1[i] * poly2[j]

    return result

def np_fft(poly1, poly2):
    target_size = 1
    required_size = len(poly1) + len(poly2) - 1
    while target_size < required_size:
        target_size *= 2

    f1 = np.pad(poly1, (0, target_size - len(poly1)))
    f2 = np.pad(poly2, (0, target_size - len(poly2)))

    F1 = np.fft.fft(f1)
    F2 = np.fft.fft(f2)
    # F = np.zeros(required_size)
    F = F1 * F2

    f = np.fft.ifft(F)
    return np.real(f[:required_size]).round()

# https://www.geeksforgeeks.org/data-science/fast-fourier-transformation-poynomial-multiplication/
def fft(a):
    n = len(a)

    # if input contains just one element
    if n == 1:
        return [a[0]]

    # For storing n complex nth roots of unity
    theta = -2 * np.pi / n

    w = np.array(list(complex(np.cos(theta * i), np.sin(theta * i)) for i in range(n)))

    # Separe coefficients
    Aeven = a[0::2]
    Aodd = a[1::2]

    # Recursive call for even indexed coefficients
    Yeven = fft(Aeven)

    # Recursive call for odd indexed coefficients
    Yodd = fft(Aodd)

    # for storing values of y0, y1, y2, ..., yn-1.
    Y = [0] * n

    middle = n // 2
    for k in range(n // 2):
        w_yodd_k = w[k] * Yodd[k]
        yeven_k = Yeven[k]

        Y[k] = yeven_k + w_yodd_k
        Y[k + middle] = yeven_k - w_yodd_k

    return Y

# https://medium.com/@positive.delta.hm/implementing-the-inverse-discrete-fourier-transform-in-python-1f53e28631c9
def ifft(a):
    n = len(a)

    # if input contains just one element
    if n == 1:
        return [a[0]]

    # For storing n complex nth roots of unity
    theta = 2 * np.pi / n

    w = np.array(list(complex(np.cos(theta * i), np.sin(theta * i)) for i in range(n)))

    # Separe coefficients
    Aeven = a[0::2]
    Aodd = a[1::2]

    # Recursive call for even indexed coefficients
    Yeven = ifft(Aeven)

    # Recursive call for odd indexed coefficients
    Yodd = ifft(Aodd)

    # for storing values of y0, y1, y2, ..., yn-1.
    Y = [0] * n

    middle = n // 2
    for k in range(n // 2):
        w_yodd_k = w[k] * Yodd[k]
        yeven_k = Yeven[k]

        Y[k] = yeven_k + w_yodd_k
        Y[k + middle] = yeven_k - w_yodd_k

    return Y


def fft_version(poly1, poly2):
    target_size = 1
    required_size = len(poly1) + len(poly2) - 1
    while target_size < required_size:
        target_size *= 2

    F1 = fft(np.pad(poly1,(0, target_size - len(poly1))))
    F2 = fft(np.pad(poly2,(0, target_size - len(poly2))))

    F = np.array(F1) * np.array(F2)
    f = np.array(ifft(F)) / target_size

    return np.real(f[:required_size]).round()

print("Bruteforce")
print(bruteforce(p1, p2))
print("Numpy")
print(np_fft(p1, p2))
print("Own")
print(fft_version(p1, p2))