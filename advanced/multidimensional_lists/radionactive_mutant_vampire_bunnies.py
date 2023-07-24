def find_player_position(data):
    """Finds the starting player position."""
    return [(row, column) for row, rows in enumerate(data) for column, symbol in enumerate(rows) if symbol == "P"][0]


def find_bunny_positions(data):
    """Finds the starting bunny positions."""
    return [(row, column) for row, rows in enumerate(data) for column, symbol in enumerate(rows) if symbol == "B"]


def expand_bunnies(starting_bunny_positions, neighbors, rows, columns, matrix):
    """Expands the bunny coverage and returns the new set of bunny positions.
       If the newly expanded bunny steps over the player, the game ends and the function returns False.
    """
    temp = []
    flag = True
    for bunny in starting_bunny_positions:
        for bunny_direction in neighbors:
            bunny_new_x = bunny[0] + neighbors[bunny_direction][0]
            bunny_new_y = bunny[1] + neighbors[bunny_direction][1]

            if 0 <= bunny_new_x < rows and 0 <= bunny_new_y < columns:
                if matrix[bunny_new_x][bunny_new_y] == "P":
                    flag = False
                matrix[bunny_new_x][bunny_new_y] = "B"
                temp.append((bunny_new_x, bunny_new_y))

    return flag, temp


def main():
    """Main function to run the game."""
    rows, columns = map(int, input().split())
    matrix = [[x for x in input()] for _ in range(rows)]

    directions = [x for x in input()]

    # Dictionary to represent neighboring moves in the matrix
    neighbors = {
        "U": (-1, 0),
        "R": (0, 1),
        "L": (0, -1),
        "D": (1, 0)
    }

    player_position = find_player_position(matrix)
    bunny_positions = find_bunny_positions(matrix)

    for direction in directions:
        new_x = player_position[0] + neighbors[direction][0]
        new_y = player_position[1] + neighbors[direction][1]

        if 0 <= new_x < rows and 0 <= new_y < columns:
            matrix[player_position[0]][player_position[1]] = "."
            player_position = (new_x, new_y)

            if matrix[new_x][new_y] == "B":
                # Bunny captures the player
                game_over, bunny_positions = expand_bunnies(bunny_positions, neighbors, rows, columns, matrix)
                status = "dead" if game_over else "won"
                print("\n".join("".join(row) for row in matrix))
                print(f"{status}: {player_position[0]} {player_position[1]}")
                break
            else:
                # Player moves and bunnies expand
                matrix[new_x][new_y] = "P"
                game_over, bunny_positions = expand_bunnies(bunny_positions, neighbors, rows, columns, matrix)

                if not game_over:
                    print("\n".join("".join(row) for row in matrix))
                    print(f"dead: {player_position[0]} {player_position[1]}")
                    break
        else:
            # Player escapes and wins the game
            x, y = player_position
            matrix[player_position[0]][player_position[1]] = "."
            game_over, bunny_positions = expand_bunnies(bunny_positions, neighbors, rows, columns, matrix)
            print("\n".join("".join(row) for row in matrix))
            print(f"won: {x} {y}")
            break


if __name__ == "__main__":
    main()
