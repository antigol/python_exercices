# edit the class A such that...
class A:
    def __init__(self, name="Paul"):
        self.name = name

    def greetings(self, ask=False):
        text = "Hello {}".format(self.name)
        if ask:
            text += ", How are you ?"
        return text


# ... all the tests pass

x = A()
assert x.name == "Paul"

x = A("John")
assert x.name == "John"

assert x.greetings() == "Hello John"

assert x.greetings(ask=True) == "Hello John, How are you ?"

