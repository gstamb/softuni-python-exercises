ROWS, COLUMNS = map(int, input().split(","))


def find_mouse_position(board):
    """ Finds the mouse's current position on the board"""
    for row, data in enumerate(board):
        for column, symbol in enumerate(data):
            if symbol == "M":
                return row, column


def find_count_cheese(board):
    """ Calculates the amount of cheese present on the map """
    return sum([1 for x in board for symbol in x if symbol == "C"])


def move_mouse(direction, board):
    """
    Finds the mouse's current position and calculates the validity of the new coordinates
    :param direction: direction to move the mouse towards.
    :param board:  the matrix
    :return: returns if the game should continue False or True
    """
    possible_mouse_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

    mouse_current_x, mouse_current_y = find_mouse_position(board)

    new_x = mouse_current_x + possible_mouse_moves[direction][0]
    new_y = mouse_current_y + possible_mouse_moves[direction][1]

    # if a valid index
    if 0 <= new_x < ROWS and 0 <= new_y < COLUMNS:
        # places the mouse on the new position
        return record_move(board, mouse_current_x, mouse_current_y, new_x, new_y)
    else:
        print("No more cheese for tonight!")
    return False


def record_move(board, mouse_current_x, mouse_current_y, new_x, new_y):
    """
    Moves the mouse to the new coordinates and records the outcome on the board.
    :param board:
    :param mouse_current_x: mouse current position rows
    :param mouse_current_y: mouse current position as columns
    :param new_x: mouse new position as rows
    :param new_y:  mouse new position as columns
    :return: returns if the game should continue False or True
    """
    value_on_new_field = board[new_x][new_y]
    if value_on_new_field == "C":
        board[mouse_current_x][mouse_current_y] = "*"
        board[new_x][new_y] = "M"
        remaining_cheese = find_count_cheese(board)
        if remaining_cheese == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            return False
        else:
            return True

    elif value_on_new_field == "T":
        board[mouse_current_x][mouse_current_y] = "*"
        board[new_x][new_y] = "M"
        print("Mouse is trapped!")
        return False
    elif value_on_new_field == "@":
        return True
    else:
        board[mouse_current_x][mouse_current_y] = "*"
        board[new_x][new_y] = "M"
        return True


def main():
    """ Main function of a mouse game.
        A mouse moves across a matrix and collects cheese or encounters traps. Based on user defined matrix size
        obstacles and direction of moves.
        The game ends:
                - Mouse consumes all the cheese fields "C" and wins.
                - Mouse is trapped if steps on "T" Field
                - Mouse  steps out of the boundaries of the matrix
                - No more commands left
    """
    matrix = [[x for x in input()] for x in range(ROWS)]

    while True:
        instruction = input()
        if instruction == "danger":
            remaining_cheese = find_count_cheese(matrix)
            if remaining_cheese > 0:
                print(f"Mouse will come back later!")
            break

        if not move_mouse(instruction, matrix):
            break

    [print("".join(x)) for x in matrix]


if __name__ == "__main__":
    main()
