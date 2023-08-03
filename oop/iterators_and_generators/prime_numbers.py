import math


def is_prime(number):
    if number < 2:
        return False
    else:
        for x in range(2, int(math.sqrt(number)) + 1):
            if number % x == 0:
                return False
        else:
            return True


def get_primes(seq):
    for number in seq:
        prime_number = is_prime(number)
        if prime_number:
            yield number
