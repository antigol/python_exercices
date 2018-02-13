# edit the class A such that...
class A:
    pass


# ... all the tests pass

x = A("Hello")
y = A("world")

print(x + y)  # prints "Hello world!"

assert len(x) == 42

assert x() == 42

assert x[42] == 42

assert 42 in x

# Bonus

x.Hello = "world !"  # prints "Hello world !"

with A("foo") as x:  # prints "foo"
    print("bar")  # prints "bar" (obviously)
    # prints "baz" when going out of the with statement
