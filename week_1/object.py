# edit the class A such that...
class A:
    pass


# ... all the tests pass

x = A()
assert x.name == "Paul"

x = A("John")
assert x.name == "John"

assert x.greetings() == "Hello John"

assert x.greetings(ask=True) == "Hello John, How are you ?"

