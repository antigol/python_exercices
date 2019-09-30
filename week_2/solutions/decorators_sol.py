from functools import wraps

def print_calls(original):
    @wraps(original)
    def decorated(*args, **kwargs):
        result = original(*args, **kwargs)

        name = original.__name__
        args = ", ".join(repr(x) for x in args)
        kwargs = ", ".join("{}={}".format(k, repr(v)) for k, v in kwargs.items())
        result = repr(result)

        print("{name}({args}, {kwargs}) = {result}".format(name=name, args=args, kwargs=kwargs, result=result))

        return result
    return decorated

@print_calls
def foo(x, y):
    return x + y


print(foo("Hello ", y="world"))



def recursive_iterator(start):
    def decorator(original):
        @wraps(original)
        def decorated(*args):
            x = start
            while True:
                yield x
                x = original(x, *args)
        return decorated
    return decorator

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
