# the size of the matrix that serves as a race route for a rally drive game
SIZE_OF_RACE_ROUTE = int(input())
#  is the identificator of players vehicle
CAR_NUMBER = input()

# keeps tracks of kilometers driven when moving around the map. the variable is required for the final output.
KILOMETERS_DRIVEN = 0

# keep track on car's current location as it enters and moves around the map
CAR_COORDINATES = (0, 0)


def find_field_location(track, obj="C"):
    """
    Function to find the location of the car or any other object on the track.
    Returns the row and column of the car's or any other object's position.
    """
    for row, columns in enumerate(track):
        for column, symbol in enumerate(columns):
            if symbol == obj:
                return row, column


def next_coordinates(direction, current_location):
    """
    The function calculates and validates new coordinates
    # Parameters:
     - direction: The direction of the next move ("up", "down", "left", or "right").
     - current_location: A tuple containing the current location in terms of (row, column) on the race field.
    # Returns
     - A new (row, column) tuple for the next location if it's within the race field boundaries.
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
    """
    Validates whether the prosed coordinates fall within the race field ( size of the matrix )
    :return: the new row and column coordinates or False if they are outside the map
    """
    if 0 <= new_x < SIZE_OF_RACE_ROUTE and 0 <= new_y < SIZE_OF_RACE_ROUTE:
        return new_x, new_y
    return False


def main():
    global KILOMETERS_DRIVEN, CAR_COORDINATES
    # ingest matrix data
    race_route = [[x for x in input().split()] for _ in range(SIZE_OF_RACE_ROUTE)]

    while True:
        # receives direction to move
        directions = input()
        if directions == "End":
            race_route[CAR_COORDINATES[0]][CAR_COORDINATES[1]] = "C"
            print(f"Racing car {CAR_NUMBER} DNF.")
            break

        # calculates the next coordinates
        next_section = next_coordinates(directions, CAR_COORDINATES)
        if next_section:
            new_x, new_y = next_section

            # records the outcome of the new location, updates car's location and keeps track on distance driven.
            next_location_val = race_route[new_x][new_y]
            # location marked "." is empty space that grants 10 kilometers millage
            if next_location_val == ".":
                race_route[new_x][new_y] = "."
                KILOMETERS_DRIVEN += 10
                CAR_COORDINATES = (new_x, new_y)
            # location marked "T" is a tunel that de-facto teleports the car to another tunnel and awards 30 points
            elif next_location_val == "T":
                race_route[new_x][new_y] = "."
                tunnel_exit = find_field_location(race_route, "T")
                tunel_exit_x, tunnel_exit_y = tunnel_exit
                race_route[tunel_exit_x][tunnel_exit_y] = "."
                KILOMETERS_DRIVEN += 30
                CAR_COORDINATES = (tunel_exit_x, tunnel_exit_y)
            # location marked "F" is the finish line. Grants 10 points of millage. Updates the map with car's last known location
            elif next_location_val == "F":
                CAR_COORDINATES = (new_x, new_y)
                race_route[new_x][new_y] = "C"
                KILOMETERS_DRIVEN += 10
                print(f"Racing car {CAR_NUMBER} finished the stage!")
                break

    # prints the distance driven and car's last known position on the racetrack
    print(f"Distance covered {KILOMETERS_DRIVEN} km.")
    [print(''.join(x)) for x in race_route]


if __name__ == "__main__":
    main()
