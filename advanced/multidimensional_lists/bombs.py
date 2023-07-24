def main():
    rows_columns = int(input())
    cells = [[int(x) for x in input().split()] for _ in range(rows_columns)]

    coordinates = input().split()

    neighbors = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

    for bomb in coordinates:
        x, y = map(int, bomb.split(","))
        if 0 <= x <= rows_columns - 1 and 0 <= y <= rows_columns - 1:
            if cells[x][y] <= 0:
                continue
            value = cells[x][y]
            cells[x][y] = 0

            for dx, dy in neighbors:
                new_x = x + dx
                new_y = y + dy

                if 0 <= new_x < rows_columns and 0 <= new_y < rows_columns and cells[new_x][new_y] > 0:
                    cells[new_x][new_y] -= value

    count_positive_elements = 0
    sum_of_positive_vals = 0
    for cell in cells:
        positive = [x for x in cell if x > 0]
        count_positive_elements += len(positive)
        sum_of_positive_vals += sum(positive)
    print(f"Alive cells: {count_positive_elements}")
    print(f"Sum: {sum_of_positive_vals}")
    [print(f"{' '.join([str(x) for x in cell])}") for cell in cells]


if __name__ == "__main__":
    main()
