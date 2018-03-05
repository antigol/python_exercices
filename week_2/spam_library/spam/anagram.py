from itertools import permutations

def anagrams(text):
    return set("".join(x) for x in permutations(text))
