#pylint: disable=E1101
import torch
from torch.autograd import Variable


def remove_row(x, i):
    if i == 0:
        return x[1:]
    if i == x.size(0) - 1:
        return x[:-1]
    return torch.cat([x[:i], x[i + 1:]])

def det(x):
    ''' computes the determinant of the matrix x '''
    assert x.size(0) == x.size(1)

    if x.size(0) == 1:
        return x[0, 0]

    to_sum = []
    for i in range(x.size(0)):
        sign = (-1) ** i
        submatrix = remove_row(x[:, 1:], i)
        minor = det(submatrix)
        to_sum += [sign * x[i, 0] * minor]
    
    return sum(to_sum)


def derivative_det_autograd(x):
    ''' computes the derivative of det(x) with respect to each component of x '''
    x = Variable(x, requires_grad=True)
    det(x).backward()
    return x.grad.data


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
