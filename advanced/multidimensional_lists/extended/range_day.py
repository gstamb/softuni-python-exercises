ROWS, COLUMNS = 5, 5


def find_shooter_position(board):
    """ Finds the player location on the map/board/matrix """
    for row, columns in enumerate(board):
        for column, symbol in enumerate(columns):
            if symbol == "A":
                return row, column


def find_all_targets(board):
    """ Finds the amount of targets on the map/board/matrix """
    return sum([1 for x in board for y in x if y == "x"])


def move(board, directions):
    """ Move the player to a specified direction and length.
        Can only step on `.` fields.
        Player's old location is replaced by an empty field `.`
     """
    _, direction, steps = directions.split()
    steps = int(steps)

    current_row, current_column = find_shooter_position(board)
    new_row, new_col = current_row, current_column
    if direction == "left":
        new_row, new_col = current_row, current_column - steps
    elif direction == "right":
        new_row, new_col = current_row, current_column + steps
    elif direction == "up":
        new_row, new_col = current_row - steps, current_column
    elif direction == "down":
        new_row, new_col = current_row + steps, current_column

    if 0 <= new_row < len(board) and 0 <= new_col < len(board) and board[new_row][new_col] == ".":
        board[new_row][new_col] = "A"
        board[current_row][current_column] = "."


def shoot(board, directions, targets_hit):
    """ Shoots at instructed direction. Can hit only one and closest target at a time. """
    _, direction = directions.split()
    current_row, current_column = find_shooter_position(board)

    if direction == "left":
        for i in range(current_column - 1, -1, -1):
            target = board[current_row][i]
            if target == "x":
                targets_hit.append((current_row, i))
                board[current_row][i] = "."
                break
    elif direction == "right":
        for i in range(current_column + 1, len(board)):
            target = board[current_row][i]
            if target == "x":
                targets_hit.append((current_row, i))
                board[current_row][i] = "."
                break
    elif direction == "down":
        for i in range(current_row + 1, len(board)):
            target = board[i][current_column]
            if target == "x":
                targets_hit.append((i, current_column))
                board[i][current_column] = "."
                break
    elif direction == "up":
        for i in range(current_row - 1, -1, -1):
            target = board[i][current_column]
            if target == "x":
                targets_hit.append((i, current_column))
                board[i][current_column] = "."
                break


def main():
    """
    Plays a shooting game on a matrix/board.

    The game involves a player (shooter) denoted by "A" and targets denoted by "x".
    The player can be moved in four directions: "up", "down", "left", and "right".
    The player can shoot targets in the specified direction, hitting the closest target.

    The game ends when all targets have been hit or when all instructions have been executed.

    Input:
    - The initial matrix, with the player and targets positioned accordingly.
    - The number of instructions to expect.
    - Instructions can be either "move <direction> <steps>" or "shoot <direction>".

    Output:
    - If all targets are hit before all instructions are executed, prints:
      "Training completed! All <number_of_targets_hit> targets hit."
      Followed by the positions of the targets hit.
    - If not all targets are hit after executing all instructions, prints:
      "Training not completed! <number_of_targets_left> targets left."
      Followed by the positions of the targets hit.
    """

    # starting size of the matrix is 5x5 by default

    # add elements to the matrix
    matrix = [[x for x in input().split()] for _ in range(ROWS)]

    # the number of instructions to expect
    number_of_instructions = int(input())

    # finds the number of targets on the board
    count_target_beginning = find_all_targets(matrix)
    targets_hit = []

    # executes each instruction
    for _ in range(number_of_instructions):
        instruction = input()
        # shoots targets down the direction upon receiving shoot instruction
        if instruction.startswith("shoot"):
            shoot(matrix, instruction, targets_hit)
            # games ends if at any point all targets have been shot
            if len(targets_hit) == count_target_beginning:
                print(f"Training completed! All {len(targets_hit)} targets hit.")
                [print(list(x)) for x in targets_hit]
                break
        # Move the player upon receiving move instructions
        elif instruction.startswith("move"):
            move(matrix, instruction)

    else:
        print(f"Training not completed! {count_target_beginning - len(targets_hit)} targets left.")
        [print(list(x)) for x in targets_hit]


if __name__ == "__main__":
    main()
