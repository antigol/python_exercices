# edit the function foo such that...
def foo(x):
    pass

# ... all the tests pass

foo(42)

try:
    foo(0)
except ValueError:
    print("It works")
else:
    print("It doesn't work")