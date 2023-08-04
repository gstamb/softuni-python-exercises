from itertools import product


def possible_permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield list(pool[i] for i in indices)


[print(n) for n in possible_permutations([1, 2, 3])]
