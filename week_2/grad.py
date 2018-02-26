import numpy as np

def minimize(f, grad_f, x0, lr, n_steps):
    """ perform n_steps of gradient descent and return the final point """
    return x0


x = minimize(lambda x: x.dot(x), lambda x: 2 * x, np.array([2, 3]), 0.1, 1000)
np.testing.assert_almost_equal(x, np.array([0, 0]))

