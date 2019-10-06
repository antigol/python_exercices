#pylint: disable=E1101
import torch


def det(x):
    ''' computes the determinant of the matrix x '''
    # Implement this function using the Laplace's formula
    # You will need a for loop and recursive calls
    raise NotImplementedError("To be implemted by the student")


def derivative_det_autograd(x):
    ''' computes the derivative of det(x) with respect to each component of x '''
    # Use the function det and .backward()
    raise NotImplementedError("To be implemted by the student")


def derivative_det_jacobi(x):
    '''
    computes the derivative using https://en.wikipedia.org/wiki/Jacobi%27s_formula
    works only if x is invertible
    '''
    return torch.transpose(torch.inverse(x) * det(x), 0, 1)


n = 7
x = torch.randn(n, n)
d_autograd = derivative_det_autograd(x)
d_jacobi = derivative_det_jacobi(x)

# check if they are similar
assert (d_autograd - d_jacobi).abs().max() < 1e-4
