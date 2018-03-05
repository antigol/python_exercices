import numpy as np


# complete this function
def mean_square_fit(x, y):
    """ Returns (a, b) such that a x + b minimize the mean square error """
    a = 1
    b = 0
    return a, b



# complete this function
def gram_schmidt(x):
    """ orthonormalize the rows of x using the Gram Schmidt prcess https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process """
    orth = []
    for i in range(len(x)):
        y = x[i]
        for j in range(i):
            y = y - np.sum(y * orth[j]) * orth[j]
        y = y / np.sum(y ** 2) ** 0.5
        orth.append(y)
    return np.stack(orth)


x = np.random.rand(10, 30)
x = gram_schmidt(x)
np.testing.assert_almost_equal(x @ x.T, np.eye(10))

