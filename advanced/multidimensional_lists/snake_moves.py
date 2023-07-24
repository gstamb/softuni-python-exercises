from collections import deque


def main():
    """ Until the dimensions of the matrix are exhausted, it fills the strings across
    rows in a snake-like pattern.

    3x4 matrix
    string = pattern

    will yield:

    patt
    pnre
    etta

    """
    # rows, columns = map(int, input().split())
    # string = input()

    rows, columns = map(int, input().split())
    string = deque([x for x in input()])

    result = []
    for row in range(rows):
        temp_arr = []

        for column in range(columns):
            letter = string.popleft()
            temp_arr.append(letter)
            string.append(letter)
        else:
            if row % 2 == 0:
                result.append(temp_arr)
            else:
                result.append(temp_arr[::-1])

    for word in result:
        print("".join(word))


if __name__ == "__main__":
    main()
