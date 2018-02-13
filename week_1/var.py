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
x += [3, 2, 1]

print(y)

x = ["hello"] * 2
x[1] += " world"

print(x)

x = [[]] * 5
x[0].append(42)

print(x)

x = [[] for _ in range(5)]
x[0].append(42)

print(x)

x = {}
x['hello'] = [1, 2, 3]
x['world'] = x['hello']
x['hello'] = [1, 2, 3, 4]

print(x)