def even_odd(*args):
    """
    Receives a list of integers and returns odd or even integers depending on command.

    :param args: sequnce of integers and instruction
    :return: list of numbers depending on the instruction
    """
    numbers = args[:-1]
    command = args[len(args) - 1]

    if command == "odd":
        return [x for x in numbers if x % 2 == 1]
    elif command == "even":
        return [x for x in numbers if x % 2 == 0]


def main():
    print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))


if __name__ == "__main__":
    main()
