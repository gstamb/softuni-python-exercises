import itertools


def generate_triplets(l):
    yield from itertools.product(*([l] * 3))


chars = [chr(x) for x in range(97, int(input()) + 97)]
for x in generate_triplets("".join(chars)):
    print(''.join(x))
