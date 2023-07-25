def find_bunny_location(board):
    """ Finds bunny's current position """
    return [(row, column) for row, field in enumerate(board) for column, cell in enumerate(field) if cell == "B"]


def count_eggs_per_direct(coordinates_bunny, matrix, field_size, direction):
    """     Moves the bunny in the specified direction and counts the number of eggs along the way.
    :param coordinates_bunny: Receives the coordinates for the bunny's current position
    :param matrix: Elements in the current board
    :param field_size:  The dimensions of the matrix board
    :param direction:  The direction for which the bunny should move
    :return: The maximum egg count , the direction and a list of moves in that direction
    """

    # gets x,y coordinates to make a move from current position
    add_x, add_y = get_direction_coordinates(direction)

    # get the bunny's current position on the board
    x = coordinates_bunny[0]
    y = coordinates_bunny[1]

    # initialize variables to hold the max egg count and moves in the direction
    count_eggs_this_direction = float('-inf')
    moves = []

    while True:
        # add coordinates to the current position
        x += add_x
        y += add_y
        # counts eggs and records coordinates if within the board and not encountering a trap "X"
        if (0 <= x < field_size and 0 <= y < field_size) and not matrix[x][y] == "X":
            # negative numbers can be encountered - corner cases check
            if count_eggs_this_direction == float('-inf'):
                count_eggs_this_direction = int(matrix[x][y])
                moves.append((x, y))
            else:
                count_eggs_this_direction += int(matrix[x][y])
                moves.append((x, y))
        else:
            break

    return count_eggs_this_direction, direction, moves


def get_direction_coordinates(direction):
    """ Returns the supplement coordinates that needs to be added to bunny current position to move """
    if direction == "up":
        return -1, 0
    elif direction == "down":
        return 1, 0
    elif direction == "left":
        return 0, -1
    elif direction == "right":
        return 0, 1


def main():
    # user input representing the size of the field
    field_size = int(input())

    # matrix containing bunny's location "B", traps "T" and eastern eggs "INT"
    matrix = [[x for x in input().split()] for _ in range(field_size)]

    # finds bunny's current location
    coordinates_bunny = find_bunny_location(matrix)[0]

    # counts the eggs in all directions
    egg_count_going_up = count_eggs_per_direct(coordinates_bunny, matrix, field_size, direction="up")
    egg_count_going_down = count_eggs_per_direct(coordinates_bunny, matrix, field_size, direction="down")
    egg_count_going_left = count_eggs_per_direct(coordinates_bunny, matrix, field_size, direction="left")
    egg_count_going_right = count_eggs_per_direct(coordinates_bunny, matrix, field_size, direction="right")

    # sort the eggs count in descending order and take the highest
    highest_egg_cnt_direction = \
        sorted([egg_count_going_up, egg_count_going_down, egg_count_going_left, egg_count_going_right],
               key=lambda x: x[0],
               reverse=True)[0]

    # print the results
    print(highest_egg_cnt_direction[1])
    for direction in highest_egg_cnt_direction[2]:
        print(list(direction))
    print(highest_egg_cnt_direction[0])


if __name__ == "__main__":
    main()
