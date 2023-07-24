def main():
    """ Finds equal 2x2 squares in a multidimensional array """
    rows, columns = map(int, input().split())
    array_contents = [[x for x in input().split()] for _ in range(rows)]

    count = 0
    for row in range(1, rows):
        for column in range(1, columns):
            a = array_contents[row - 1][column - 1]
            b = array_contents[row - 1][column]
            c = array_contents[row][column - 1]
            d = array_contents[row][column]
            if len(set([a, b, c, d])) == 1:
                count += 1

    print(count)


if __name__ == "__main__":
    main()
