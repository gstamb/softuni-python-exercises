from collections import deque
from functools import reduce
from math import floor


def perform_arithmetics(digits, item):
    """
    Performs arithmetics on all the digits from the queue.
    Resulting number is either the result or will be used in subsequence calculations.
    """
    result = 0
    if digits:
        if item == "*":
            result = reduce(lambda x, y: x * y, digits)
        elif item == "/":
            result = reduce(lambda x, y: x / y, digits)
        elif item == "+":
            result = reduce(lambda x, y: x + y, digits)
        elif item == "-":
            result = reduce(lambda x, y: x - y, digits)
    digits.clear()
    digits.append(floor(result))


def main():
    sequence = input().split()
    digits = deque()
    for item in sequence:
        if item.isdigit():
            digits.append(int(item))
        # need to check for a negative number
        elif item.startswith("-") and len(item) > 1:
            digits.append(int(item))
        # else will be an operator
        else:
            perform_arithmetics(digits, item)

    if digits:
        [print(item) for item in digits]


if __name__ == "__main__":
    main()
