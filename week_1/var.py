x = 42

print(x)

y = x
x += 100

print(y)

x = "hello"
y = x
x += " world"

print(y)

x = [1, 2, 3]
y = x
x = [3, 2, 1]

print(y)

x = [1, 2, 3]
y = x
x[:] = [3, 2, 1]

print(y)

x = [1, 2, 3]
y = x
x += [3, 2, 1]

print(y)

x = ["hello"] * 2
x[1] += " world"

print(x)

x = [[]] * 5
x[0].append(42)

print(x)

x = [[]] * 5
x[0] = 42

print(x)

x = [[] for _ in range(5)]
x[0].append(42)

print(x)

x = {}
x['hello'] = [1, 2, 3]
x['world'] = x['hello']
x['hello'] = [1, 2, 3, 4]

print(x)


def foo1(x):
    x += " world!"
x = "hello"
foo1(x)
print(x)


def foo2(x):
    x += [42]
x = []
foo2(x)
print(x)


def foo3(x):
    x = sorted(x)
x = [3, 2, 1]
foo3(x)
print(x)


def foo4(x):
    x[:2] = [42, 42]
x = [0, 0, 0]
foo4(x)
print(x)


try:
    x = ([1, 2, 3], 42)
    x[0][:] = []
    x[1] += 10
    print(x)
except Exception as e:
    print(e)
