# edit the function foo such that...
def foo(x):
    if x == 0:
        raise ValueError()


# ... all the tests pass

foo(42)

try:
    foo(0)
except ValueError:
    print("It works")
else:
    print("It doesn't work")