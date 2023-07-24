def main():
    """ Creates lists containing the primary and the secondary diagonal elements of a multidimensional list.
        Prints the elements and their sum.
    """
    dimensions = int(input())
    nested_list = [[int(x) for x in input().split(", ")] for _ in range(dimensions)]

    primary_diagonal = [nested_list[index][position] for index, row in
                        enumerate(nested_list) for position, element in enumerate(row) if
                        index - position == 0]

    secondary_diagonal = [nested_list[index][position] for index, row in
                          enumerate(nested_list) for position, element in enumerate(row) if
                          index + position == dimensions - 1]
    print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
    print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")


if __name__ == "__main__":
    main()
