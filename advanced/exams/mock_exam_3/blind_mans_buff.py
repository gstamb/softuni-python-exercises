ROWS, COLUMNS = map(int, input().split())
TOUCHED = 0
MOVES = 0


def find_player_position(board):
    """ Finds the player's current position """
    for row, data in enumerate(board):
        for column, symbol in enumerate(data):
            if symbol == "B":
                return row, column


def move_player(board, current_player_location, direction):
    """ Calculates the new player position as x,y index """
    current_x, current_y = current_player_location
    if direction == "up":
        return validate_new_coodinates(current_x - 1, current_y)
    elif direction == "down":
        return validate_new_coodinates(current_x + 1, current_y)
    elif direction == "left":
        return validate_new_coodinates(current_x, current_y - 1)
    elif direction == "right":
        return validate_new_coodinates(current_x, current_y + 1)


def validate_new_coodinates(new_x, new_y):
    """ Validates that the new index is within the borders of the matrix """
    if 0 <= new_x < ROWS and 0 <= new_y < COLUMNS:
        return new_x, new_y
    return False


def count_players(board):
    """ Counts the remaining players on the board"""
    return sum([1 for x in board for y in x if y == "P"])


def main():
    """
    Main function of the game Blind Man's Buff.
    Ingests initial input.
    Processes the directional commands.
    Moves the player and records moves across the matrix.
        letters on the map stands as follows:
        "P" - players to be caught can be stepped on
        "O" - obstacle that cannot be stepped on
        "-" - empty space that can be stepped on
        "B" - Main player location

    Keep track on TOUCHED and MOVES variable that record players who have been caught
    and number of legitimate moves ( fields it can be stepped on).

    Game ends when the commands have been exhausted or all players have been caught.
    """
    global TOUCHED, MOVES
    matrix = [[x for x in input().split()] for _ in range(ROWS)]

    while True:
        instruction = input()
        if instruction == "Finish":
            break

        current_location = find_player_position(matrix)
        next_coordinates = move_player(matrix, current_location, instruction)
        if next_coordinates:
            old_x, old_y = current_location
            new_x, new_y = next_coordinates
            if matrix[new_x][new_y] == "O":
                continue
            elif matrix[new_x][new_y] == "P":
                TOUCHED += 1
                MOVES += 1
                matrix[old_x][old_y] = "-"
                matrix[new_x][new_y] = "B"
                if count_players(matrix) == 0:
                    break
            elif matrix[new_x][new_y] == "-":
                MOVES += 1
                matrix[old_x][old_y] = "-"
                matrix[new_x][new_y] = "B"

    print("Game over!")
    print(f"Touched opponents: {TOUCHED} Moves made: {MOVES}")


if __name__ == "__main__":
    main()
