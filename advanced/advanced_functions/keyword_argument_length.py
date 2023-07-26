def kwargs_length(**kwargs) -> int:
    """ Receives unpacked name and age from a dictionary and returns their length"""
    return len(kwargs)


def main():
    dictionary = {'name': 'Peter', 'age': 25}
    print(kwargs_length(**dictionary))


if __name__ == "__main__":
    main()
