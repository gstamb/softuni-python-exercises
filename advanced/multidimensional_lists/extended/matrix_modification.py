def main():
    """ Modifies elements in a multidimensional array """
    rows_columns_matrix = int(input())
    matrix = [[int(x) for x in input().split()] for _ in range(rows_columns_matrix)]

    while True:
        # Get the instruction from the user
        instruction = input()

        # Check if the user wants to end the process
        if instruction == "END":
            break

        if instruction.startswith("Add"):
            # Parse the coordinates and value to be added
            x, y, val = map(int, instruction[3:].split())
            if 0 <= x < rows_columns_matrix and 0 <= y < rows_columns_matrix:
                # Modify the element at the specified coordinates
                matrix[x][y] += val
            else:
                print("Invalid coordinates")
        elif instruction.startswith("Subtract"):
            # Parse the coordinates and value to be subtracted
            x, y, val = map(int, instruction[8:].split())
            if 0 <= x < rows_columns_matrix and 0 <= y < rows_columns_matrix:
                # Modify the element at the specified coordinates
                matrix[x][y] -= val
            else:
                print("Invalid coordinates")

    # Print the modified matrix
    [print(" ".join([str(x) for x in row])) for row in matrix]


if __name__ == "__main__":
    main()
