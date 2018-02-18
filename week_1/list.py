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

ys = []  # modify this line
assert xs == ys



xs = []
for i in range(42):
    if i % 3 != 0:
        xs.append(i)

ys = []  # modify this line
assert xs == ys



xs = []
for i in range(42):
    tmp = []
    for j in range(i):
        if i + j < 42:
            tmp.append(i + j)
    xs.append(tmp)

ys = []  # modify this line
assert xs == ys



# given zs
zs = [3, 0, 2, 0, 0, 4, 3, 0]

xs = []
for i, z in enumerate(zs):
    if z == 0:
        xs.append(i)

ys = []  # do the same in one line
assert xs == ys



xs = []
for i in range(42):
    xs.append((i, 'a'))
    xs.append((i, 'b'))
    xs.append((i, 'c'))

ys = []  # modify this line
assert xs == ys



xs = {}
for i in range(10):
    xs[i] = str(i)

ys = {}  # modify this line
assert xs == ys



xs = []
for i in range(2, 50):
    is_prime = True
    for k in range(2, i):
        if i % k == 0:
            is_prime = False
    if is_prime:
        xs.append(i)

ys = []  # modify this line
assert xs == ys


