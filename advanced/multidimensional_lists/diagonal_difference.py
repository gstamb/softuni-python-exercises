def main():
    """ Calculates the absolute difference between the primary and the secondary diagonal of a multidimensional list"""
    dimensions = int(input())
    nested_list = [[int(x) for x in input().split()] for _ in range(dimensions)]

    primary_diagonal = [nested_list[index][position] for index, row in
                        enumerate(nested_list) for position, element in enumerate(row) if
                        index - position == 0]

    secondary_diagonal = [nested_list[index][position] for index, row in
                          enumerate(nested_list) for position, element in enumerate(row) if
                          index + position == dimensions - 1]
    print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))


if __name__ == "__main__":
    main()
