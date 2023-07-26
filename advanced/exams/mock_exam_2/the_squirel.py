from collections import deque

MATRIX_SIZE = int(input())
TARGET_HAZELNUTS = 3


def find_squirrel_index(board):
    """ Finds the squirrel position on the board"""
    for row, data in enumerate(board):
        for column, symbol in enumerate(data):
            if symbol == "s":
                return row, column


def move_squirrel(direction, current_location):
    """
    Calculates and triggers validation of the new coordinates
    :param direction: the direction toward which the squirrel should move
    :param current_location the current location of the squirrel
    :return: new coordinates if valid
    """
    current_x, current_y = current_location
    new_x, new_y = "", ""
    if direction == "left":
        new_x, new_y = current_x, current_y - 1
    elif direction == "right":
        new_x, new_y = current_x, current_y + 1
    elif direction == "up":
        new_x, new_y = current_x - 1, current_y
    elif direction == "down":
        new_x, new_y = current_x + 1, current_y
    return validate_coordinates(new_x, new_y)


def validate_coordinates(x, y):
    """
    Returns thew new coordinates if these are within the board
    """
    if 0 <= x < MATRIX_SIZE and 0 <= y < MATRIX_SIZE:
        return x, y
    return False


def main():
    """
    Main function that runs the squirrel game. Squirrel moves across the board collecting hazelnuts.
    There are 4 possible results:
        ⦁	You win if the squirrel collects 3 of the hazelnuts.
        ⦁	The squirrel collects less than 3 hazelnuts.
        ⦁	The squirrel steps on a trap.
        ⦁	The squirrel moves out of the field.
    The function moves the squirrel across the map and records its position and collects hazelnuts.
    Prints the outcome and the amount of Hazelnuts collected

    """
    global TARGET_HAZELNUTS
    directions = deque(input().split(", "))
    matrix = [[x for x in input()] for _ in range(MATRIX_SIZE)]

    while directions:
        direction = directions.popleft()
        current_position = find_squirrel_index(matrix)

        new_coordinates = move_squirrel(direction, current_position)
        if new_coordinates:
            old_x, old_y = current_position
            new_x, new_y = new_coordinates
            if matrix[new_x][new_y] == "h":
                TARGET_HAZELNUTS -= 1
                matrix[old_x][old_y] = "*"
                matrix[new_x][new_y] = "s"
                if TARGET_HAZELNUTS == 0:
                    print("Good job! You have collected all hazelnuts!")
                    break

            elif matrix[new_x][new_y] == "t":
                print("Unfortunately, the squirrel stepped on a trap...")
                break

            elif matrix[new_x][new_y] == "*":
                matrix[old_x][old_y] = "*"
                matrix[new_x][new_y] = "s"

        else:
            print("The squirrel is out of the field.")
            break
    else:
        print("There are more hazelnuts to collect.")

    print(f"Hazelnuts collected: {3 - TARGET_HAZELNUTS}")


if __name__ == "__main__":
    main()
