# Implement the print_calls function decorator that prints each function calls

@print_calls
def foo(x, y):
    return x + y


print(foo("Hello ", "world"))
# Should print "foo('Hello ', 'world') = 'Hello world' on one line then print "Hello world" on the second line



"""
Implement a decorator called recursive_iterator that convert an function into an iterator

You can make a decorator that takes something in argument by making a function that returns a decorator!

Given a function F(z, *args) we want an iterator that generate z0, F(z0, *args), F(F(z0, *args), *args), ...
"""

@recursive_iterator(10)
def inc(x):
    return x + 1

i = inc()
assert next(i) == 10
assert next(i) == 11
assert next(i) == 12
assert next(i) == 13


@recursive_iterator(0)
def mandlebrot(z, c):
    return z ** 2 + c


c = -0.1011 + 0.9563j
i = mandlebrot(c)
assert next(i) == 0
assert next(i) == c
assert next(i) == c ** 2 + c
