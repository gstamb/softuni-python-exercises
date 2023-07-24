def main():
    """ Calculates the maximum sum of 3x3 square elements """
    rows, columns = map(int, input().split())
    arrays_contents = [[int(x) for x in input().split()] for _ in range(rows)]
    max_sum = float('-inf')
    result_square = []
    for row in range(1, rows - 1):
        for column in range(1, columns - 1):
            a = arrays_contents[row - 1][column - 1]
            b = arrays_contents[row - 1][column]
            c = arrays_contents[row - 1][column + 1]

            d = arrays_contents[row][column - 1]
            e = arrays_contents[row][column]
            f = arrays_contents[row][column + 1]

            g = arrays_contents[row + 1][column - 1]
            h = arrays_contents[row + 1][column]
            i = arrays_contents[row + 1][column + 1]

            current_sum = sum([a, b, c, d, e, f, g, h, i])
            if current_sum > max_sum:
                max_sum = current_sum
                result_square = [[a, b, c], [d, e, f], [g, h, i]]

    print(f"Sum = {max_sum}")
    for row in result_square:
        # print(row)
        print(" ".join([str(x) for x in row]))


if __name__ == "__main__":
    main()
