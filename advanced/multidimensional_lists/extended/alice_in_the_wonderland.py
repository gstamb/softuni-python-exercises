def find_alice_position(board):
    """ Finds Alice's location """
    for row, data in enumerate(board):
        for column, element in enumerate(data):
            if element == "A":
                return row, column


def main():
    """ Alice moves across a board and collects teabags.
        Program ends if she steps on a rabbit hole "R", runs outside the board or collects enough teabags.
    """
    # receive input about size of the matrix
    size_matrix = int(input())

    # elements of the matrix
    matrix = [[x for x in input().split()] for _ in range(size_matrix)]

    # find location of Alice
    alice_location = find_alice_position(matrix)

    # alice can move up , down , left and right
    possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, +1)}

    # variable to keep track of collected teabags
    collected_teabags = 0

    while True:
        move_alice_direction = input()

        # Alice's new position on the board
        new_x = alice_location[0] + possible_moves[move_alice_direction][0]
        new_y = alice_location[1] + possible_moves[move_alice_direction][1]

        # if Alice's new location is a valid index, move Alice.
        if 0 <= new_x < size_matrix and 0 <= new_y < size_matrix:
            # when moved, Alice's old position is marked as visited.
            matrix[alice_location[0]][alice_location[1]] = "*"

            # check the value of the new location:
            new_location = matrix[new_x][new_y]

            # if Alice's steps on a rabit hole , game ends
            if new_location == "R":
                matrix[new_x][new_y] = "*"
                print("Alice didn't make it to the tea party.")
                [print(" ".join(x)) for x in matrix]
                break
            # if Alice steps on an empty space. Insert Alice's id and update current position
            elif new_location == ".":
                matrix[new_x][new_y] = "A"
                alice_location = (new_x, new_y)

            # if Alice returns to previous visited place. only update current position.
            elif new_location == "*":
                alice_location = (new_x, new_y)
            else:
                # if Alice steps on a teabag. Collect amount and update current position
                matrix[new_x][new_y] = "A"
                collected_teabags += int(new_location)
                alice_location = (new_x, new_y)
                # check if enough teabags are collected
                if collected_teabags >= 10:
                    matrix[alice_location[0]][alice_location[1]] = "*"
                    print("She did it! She went to the party.")
                    [print(" ".join(x)) for x in matrix]
                    break
        # if Alice steps outside the boundary of the board the game ends
        else:
            matrix[alice_location[0]][alice_location[1]] = "*"
            print("Alice didn't make it to the tea party.")
            [print(" ".join(x)) for x in matrix]
            break


if __name__ == "__main__":
    main()
