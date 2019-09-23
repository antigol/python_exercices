# Simplify these functions using python built-ins

def sort(xs):
    """Return the list sorted"""
    return sorted(xs)

def unique(xs):
    """Return a list without duplicates"""
    # Unfortunately this solutions does not preserves the order
    return list(set(xs))

def min_of_two_lists(xs, ys):
    """Return the minimum value of the two lists"""
    return min(*xs, *ys)

def transpose(xs):
    """Return the transpose of a list of lists"""
    return [list(i) for i in zip(*xs)]

