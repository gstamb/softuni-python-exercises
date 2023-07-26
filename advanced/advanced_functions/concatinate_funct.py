def concatenate(*args, **kwargs):
    """
    Concatenates the strings in args.
    Replaces keyword argument key with its value if it exists.
    :param args: list of strings
    :param kwargs: list of key value pairs
    :return: resulting string
    """
    concatenated_string = "".join(args)

    for key, value in kwargs.items():
        if key in concatenated_string:
            concatenated_string = concatenated_string.replace(key, value)
    return concatenated_string


def main():
    print(concatenate("I", " ", "Love", " ", "Cythons",
                      C="P", s="", java='Java'))


if __name__ == "__main__":
    main()
