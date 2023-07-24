def main():
    """ Swaps elements in a multidimensional array """
    rows, columns = map(int, input().split())
    matrix_data = [[x for x in input().split()] for _ in range(rows)]

    while True:
        instruction = input()
        if instruction == "END":
            break
        # need to validate four coordinates following swap
        if instruction.startswith("swap") and len(instruction[4:].split()) == 4:
            x1, y1, x2, y2 = map(int, instruction[4:].split())
            if 0 <= x1 <= rows - 1 and 0 <= y1 <= columns - 1 and 0 <= x2 <= rows - 1 and 0 <= y2 <= columns - 1:

                matrix_data[x1][y1], matrix_data[x2][y2] = matrix_data[x2][y2], matrix_data[x1][y1]

                for row in matrix_data:
                    print(" ".join([str(x) for x in row]))
            else:
                print("Invalid input!")
        else:
            print("Invalid input!")


if __name__ == "__main__":
    main()
