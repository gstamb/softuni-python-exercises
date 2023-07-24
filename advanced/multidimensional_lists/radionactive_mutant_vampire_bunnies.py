def get_player_position(data):
    """ Get the starting player position """
    return [(row, column) for row, rows in enumerate(data) for column, symbol in enumerate(rows) if symbol == "P"][0]


def get_bunny_position(data):
    """ Get the starting bunny position """
    return [(row, column) for row, rows in enumerate(data) for column, symbol in enumerate(rows) if symbol == "B"]


def expand_bunny(starting_bunny_position, neighbours, rows, columns, matrix):
    """ Expands the bunny coverage and returns the new set of bunnies positions.
        If the newly expanded bunny steps over the player. The game ends and the function returns False
    """
    temp = []
    flag = True
    for bunny in starting_bunny_position:
        for bunny_direction in neighbours:
            bunny_new_x = bunny[0] + neighbours[bunny_direction][0]
            bunny_new_y = bunny[1] + neighbours[bunny_direction][1]

            if 0 <= bunny_new_x <= rows - 1 and 0 <= bunny_new_y <= columns - 1:
                if matrix[bunny_new_x][bunny_new_y] == "P":
                    flag = False
                matrix[bunny_new_x][bunny_new_y] = "B"
                temp.append((bunny_new_x, bunny_new_y))
    if not flag:
        return flag

    return temp


def main():
    """
    """
    rows, columns = map(int, input().split())
    matrix = [[x for x in input()] for _ in range(rows)]

    directions = [x for x in input()]
    # Dictionary to represent neighboring moves in the matrix
    neighbours = {
        "U": (-1, 0),
        "R": (0, 1),
        "L": (0, -1),
        "D": (1, 0)
    }
    current_position = get_player_position(matrix)

    starting_bunny_position = get_bunny_position(matrix)

    # loop over the list of players moves
    for direction in directions:
        new_x = current_position[0] + neighbours[direction][0]
        new_y = current_position[1] + neighbours[direction][1]

        if 0 <= new_x <= rows - 1 and 0 <= new_y <= columns - 1:
            matrix[current_position[0]][current_position[1]] = "."
            current_position = (new_x, new_y)
            # if the new position is already occupied by a bunny - the game ends.
            if matrix[new_x][new_y] == "B":
                # We need to expand on bunny new position for final display
                starting_bunny_position = expand_bunny(starting_bunny_position, neighbours, rows, columns, matrix)
                for row in matrix:
                    print("".join(row))
                print(f"dead: {current_position[0]} {current_position[1]}")
                break
            else:
                # else we expand the player and add new set of bunnies
                matrix[new_x][new_y] = "P"
                starting_bunny_position = expand_bunny(starting_bunny_position, neighbours, rows, columns, matrix)
                # if the newly created bunnies step over the player - the game ends.
                if not starting_bunny_position:
                    for row in matrix:
                        print("".join(row))
                    print(f"dead: {current_position[0]} {current_position[1]}")
                    break
        else:
            # if index is not within range - the player has escaped. The game is won.
            x, y = current_position
            # we remove the player from the map, expand the bunny one final time and print the final state of the map.
            matrix[current_position[0]][current_position[1]] = "."
            starting_bunny_position = expand_bunny(starting_bunny_position, neighbours, rows, columns, matrix)
            for row in matrix:
                print("".join(row))
            print(f"won: {x} {y}")
            break


if __name__ == "__main__":
    main()
