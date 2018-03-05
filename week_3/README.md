# Week 3 : Pytorch

Give a look at the following links:
- [http://pytorch.org/](http://pytorch.org/)
- [http://pytorch.org/docs/](http://pytorch.org/docs/)
- [http://pytorch.org/tutorials/](http://pytorch.org/tutorials/)

## autograd

The following exercise shows the power of `torch.autograd` to compute derivatives of complicated expressions.
It can compute the derivative of expressions even if the expression has been defined using for loops and recursive functions.

Let `M` be a `n` by `n` matrix
Compute the derivative of `det(M)` with respect to each componant of `M`
Complete the file `autograd.py`

## MNIST

The file `mnist.py` contains a minimalist example to classify MNIST (the digits from 0 to 9)
