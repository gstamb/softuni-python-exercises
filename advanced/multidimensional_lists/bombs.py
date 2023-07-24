def count_positive_elements(matrix):
    return sum(1 for row in matrix for val in row if val > 0)


def sum_of_positive_vals(matrix):
    return sum(val for row in matrix for val in row if val > 0)


def main():
    """ 'Explodes' element and its neighbouring cells based on multidimensional array and coordinates.
         Prints the count and sum of all remaining positive numbers as well as the final matrix.
    """
    rows_columns = int(input())
    cells = [[int(x) for x in input().split()] for _ in range(rows_columns)]

    coordinates = input().split()

    neighbors = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

    for bomb in coordinates:
        x, y = map(int, bomb.split(","))
        if 0 <= x <= rows_columns - 1 and 0 <= y <= rows_columns - 1:
            # bombs with 0 value cannot explode
            if cells[x][y] <= 0:
                continue

            # bombs yield can be reduced due to previous explosions, so we need to reevaluate that here
            value = cells[x][y]
            cells[x][y] = 0

            # creates coordinates of all possible neighbouring cells
            for dx, dy in neighbors:
                new_x = x + dx
                new_y = y + dy

                # validates that the new coordinates fall within the range of the matrix
                if 0 <= new_x < rows_columns and 0 <= new_y < rows_columns and cells[new_x][new_y] > 0:
                    cells[new_x][new_y] -= value

    # prints the requirements
    positive_elements_cnt = count_positive_elements(cells)
    sum_positive_vals = sum_of_positive_vals(cells)
    print(f"Alive cells: {positive_elements_cnt}")
    print(f"Sum: {sum_positive_vals}")
    [print(f"{' '.join([str(x) for x in cell])}") for cell in cells]


if __name__ == "__main__":
    main()
