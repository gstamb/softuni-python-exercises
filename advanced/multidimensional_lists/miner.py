def get_coal_count(data):
    return sum(1 for rows in data for symbol in rows if symbol == "c")


def get_starting_position(data):
    return [(row, column) for row, rows in enumerate(data) for column, symbol in enumerate(rows) if symbol == "s"][0]


def main():
    """Game of a miner who moves across a map and collects coal based on user-provided directions.
    The game ends when the miner encounters a symbol on the map or the directions are exhausted.
    """
    matrix_size = int(input())
    commands = input().split()
    matrix = [[x for x in input().split()] for _ in range(matrix_size)]

    # Dictionary to represent neighboring moves in the matrix
    neighbours = {
        "up": (-1, 0),
        "right": (0, 1),
        "left": (0, -1),
        "down": (1, 0)
    }
    current_index = get_starting_position(matrix)

    total_coal_available = get_coal_count(matrix)
    coal_collected = 0

    for command in commands:
        new_x = current_index[0] + neighbours[command][0]
        new_y = current_index[1] + neighbours[command][1]

        if 0 <= new_x <= matrix_size - 1 and 0 <= new_y <= matrix_size - 1:
            value_current_location = matrix[new_x][new_y]
            current_index = (new_x, new_y)

            if value_current_location == "c":
                coal_collected += 1
                matrix[new_x][new_y] = "*"
            elif value_current_location == "e":
                print(f"Game over! {current_index}")
                break
    else:
        if total_coal_available == coal_collected:
            print(f"You collected all coal! {current_index}")
        else:
            print(f"{total_coal_available - coal_collected} pieces of coal left. {current_index}")


if __name__ == "__main__":
    main()
