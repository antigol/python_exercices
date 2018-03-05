import numpy as np

def minimize(f, grad_f, x0, lr, n_steps):
    """ perform n_steps of gradient descent and return the final point """
    x = x0
    for _ in range(n_steps):
        x = x - lr * grad_f(x)
    return f(x)


x = minimize(lambda x: x.dot(x), lambda x: 2 * x, np.array([2, 3]), 0.1, 1000)
np.testing.assert_almost_equal(x, np.array([0, 0]))

