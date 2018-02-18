# Simplify these functions using python built-ins

# For example,
def sort(xs):
    """Return the list sorted"""
    n = len(xs)

    if n <= 1:
        return xs

    left = sort(xs[:n // 2])
    right = sort(xs[n // 2:])

    output = []
    while left and right:
        smallest = left.pop(0) if left[0] <= right[0] else right.pop(0)
        output.append(smallest)
    return output + left + right
# can be simplified by the built-in function sorted


# Using the built-in type set, simplifies this function
def unique(xs):
    """Return a list without duplicates"""
    ys = []
    for x in xs:
        if not x in ys:
            ys.append(x)
    return ys


# Using * simplifies this function
def min_of_two_lists(xs, ys):
    """Return the minimum value of the two lists"""
    return min(min(xs), min(ys))


# Using a list comprehension and zip, simplifies this function
def transpose(xs):
    """Return the transpose of a list of lists"""
    n = min(len(x) for x in xs)
    ys = []
    for i in range(n):
        ys.append([])
        for j in range(len(xs)):
            ys[-1].append(xs[j][i])
    return ys
