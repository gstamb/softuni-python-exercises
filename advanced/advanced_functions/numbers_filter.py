def even_odd_filter(**kwargs):
    """
    Filters odd or even numbers in the corresponding list.

    :param kwargs: number of named arguments containing `odd` or `even` as keys and a list of numbers
    :return: a dictionary containing the corresponding `odd` or `even` values as a list
    """
    result_dict = {}
    if "even" in kwargs:
        result_dict["even"] = [x for x in kwargs["even"] if x % 2 == 0]
    if "odd" in kwargs:
        result_dict["odd"] = [x for x in kwargs["odd"] if x % 2 == 1]

    return result_dict


def main():
    print(even_odd_filter(
        odd=[1, 2, 3, 4, 10, 5],
        even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
    ))


if __name__ == "__main__":
    main()
