# Convert the following codes into one line

# Example
xs = []
for i in range(42):
    xs.append(i)

ys = [i for i in range(42)]
assert xs == ys



xs = []
for i in range(42):
    xs.append(2 * i + 1)

ys = [2 * i + 1 for i in range(42)]
assert xs == ys



xs = []
for i in range(42):
    if i % 3 != 0:
        xs.append(i)

ys = [i for i in range(42) if i % 3 != 0]
assert xs == ys



xs = []
for i in range(42):
    tmp = []
    for j in range(i):
        if i + j < 42:
            tmp.append(i + j)
    xs.append(tmp)

ys = [[i + j for j in range(i) if i + j < 42] for i in range(42)]
assert xs == ys



# given zs
zs = [3, 0, 2, 0, 0, 4, 3, 0]

xs = []
for i, z in enumerate(zs):
    if z == 0:
        xs.append(i)

ys = [i for i, z in enumerate(zs) if z == 0]
assert xs == ys



xs = []
for i in range(42):
    xs.append((i, 'a'))
    xs.append((i, 'b'))
    xs.append((i, 'c'))

ys = [(i, j) for i in range(42) for j in ['a', 'b', 'c']]
assert xs == ys



xs = {}
for i in range(10):
    xs[i] = str(i)

ys = {i : str(i) for i in range(10)}
assert xs == ys



xs = []
for i in range(2, 50):
    is_prime = True
    for k in range(2, i):
        if i % k == 0:
            is_prime = False
    if is_prime:
        xs.append(i)

ys = [i for i in range(2, 50) if not any([i % k == 0 for k in range(2, i)])]
assert xs == ys


