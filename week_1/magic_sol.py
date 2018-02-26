# edit the class A such that...
class A:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return A(self.x + " " + other.x + "!")

    def __repr__(self):
        return self.x

    def __len__(self):
        return 42

    def __call__(self):
        return 42

    def __getitem__(self, i):
        return i

    def __contains__(self, i):
        return i == 42

    def __setattr__(self, name, value):
        if name == "Hello":
            print("{} {}".format(name, value))
        else:
            # we need to call the super class setattr otherwise in the constructor
            #     self.x = x
            # would not create a new attribute
            super().__setattr__(name, value)

    def __enter__(self):
        print(self.x)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("baz")



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
