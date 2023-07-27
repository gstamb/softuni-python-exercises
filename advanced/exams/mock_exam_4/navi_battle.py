# determines the size of the battlefield
SIZE_OF_BATTLEFIELD = int(input())
# determines the current health of the submarine
MINE_HIT_LIMIT = 3
# keep track on win condition of destroying ships
BATTLE_CRUISERS_LEFT = 3


def find_submarine_location(ocean):
    """
    Function to find the location of the submarine (`S`) on the battlefield.
    Returns the row and column of the submarine's position.
    """
    for row, columns in enumerate(ocean):
        for column, symbol in enumerate(columns):
            if symbol == "S":
                return row, column


def next_coordinates(direction, current_location):
    """
    The function calculates and validates new coordinates
    # Parameters:
     - direction: The direction of the next move ("up", "down", "left", or "right").
     - current_location: A tuple containing the current location in terms of (row, column) on the matrix.
    # Returns
     - A new (row, column) tuple for the next location if it's within the battlefield boundaries.
    """
    current_x, current_y = current_location
    if direction == "left":
        return validate_new_coordinates(current_x, current_y - 1)
    elif direction == "right":
        return validate_new_coordinates(current_x, current_y + 1)
    elif direction == "up":
        return validate_new_coordinates(current_x - 1, current_y)
    elif direction == "down":
        return validate_new_coordinates(current_x + 1, current_y)


def validate_new_coordinates(new_x, new_y):
    if 0 <= new_x < SIZE_OF_BATTLEFIELD and 0 <= new_y < SIZE_OF_BATTLEFIELD:
        return new_x, new_y
    return False


def main():
    """
    Main function of Navi Battle game. A submarine (marked as "S") is navigating across an ocean,
    seeking to destroy enemy cruiser ships (marked as "C").
    Game continues until all enemy ships are destroyed
    or the submarine takes irreparable damage due to running on sea mines (Marked as "*").
    :return:
    """
    global SIZE_OF_BATTLEFIELD, MINE_HIT_LIMIT, BATTLE_CRUISERS_LEFT
    battlefield_matrix = [[x for x in input()] for _ in range(SIZE_OF_BATTLEFIELD)]

    # receives directions until all cruisers are destroyed or enough damage is taken
    while True:
        move_direction = input()
        if move_direction not in ["up", "down", "left", "right"]:
            break

        # finds current location of the submarine
        current_location = find_submarine_location(battlefield_matrix)

        # calculates and validates the new location.
        new_coordinates = next_coordinates(move_direction, current_location)
        if new_coordinates:
            old_x, old_y = current_location
            new_x, new_y = new_coordinates

            # extracting the value of the next field to account for mines and destroyed cruisers
            next_location_val = battlefield_matrix[new_x][new_y]
            if next_location_val == "C":
                BATTLE_CRUISERS_LEFT -= 1
                battlefield_matrix[old_x][old_y] = "-"
                battlefield_matrix[new_x][new_y] = "S"
                if BATTLE_CRUISERS_LEFT == 0:
                    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                    [print("".join(x)) for x in battlefield_matrix]
                    break

            elif next_location_val == "*":
                MINE_HIT_LIMIT -= 1
                battlefield_matrix[old_x][old_y] = "-"
                battlefield_matrix[new_x][new_y] = "S"
                if MINE_HIT_LIMIT == 0:
                    print(f"Mission failed, U-9 disappeared! Last known coordinates [{new_x}, {new_y}]!")
                    [print("".join(x)) for x in battlefield_matrix]
                    break
            elif next_location_val == "-":
                battlefield_matrix[old_x][old_y] = "-"
                battlefield_matrix[new_x][new_y] = "S"


if __name__ == "__main__":
    main()
