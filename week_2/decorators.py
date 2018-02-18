# Implement the print_calls function decorator that prints each function calls

@print_calls
def foo(x, y):
    return x + y


print(foo("Hello ", "world"))
# Should print "foo('Hello ', 'world') = 'Hello world' on one line then print "Hello world" on the second line
