def find_knight_indexes(board):
    """ Return the coordinates of each knight """
    return [(row, column) for row, numbers in enumerate(board) for column, symbol in enumerate(numbers) if
            symbol == "K"]


def main():
    """
     Input is a chess board containing multiple knights.
     The goal is remove knights from a chess board until no knight can take another knight within one move.
     The knight with the highest possible captures is taken away from the board in each iteration.
      """
    # initial input of board size
    rows_columns = int(input())
    # "0" empty square or "K" knights on the board
    matrix = [[x for x in input()] for _ in range(rows_columns)]

    # Get the coordinates of each knight on the board
    knight_indexes = find_knight_indexes(matrix)

    # possible moves of each knight
    possible_knight_moves = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

    # count removals until no possible captures
    count = 0
    while knight_indexes:
        knights_data_coordinates_captures = {}
        for knight in knight_indexes:
            for move in possible_knight_moves:
                possible_position_on_x = knight[0] + move[0]
                possible_position_on_y = knight[1] + move[1]
                if 0 <= possible_position_on_x < rows_columns and 0 <= possible_position_on_y < rows_columns:
                    if matrix[possible_position_on_x][possible_position_on_y] == "K":
                        if knight not in knights_data_coordinates_captures:
                            knights_data_coordinates_captures[knight] = 1
                        else:
                            knights_data_coordinates_captures[knight] += 1

        if knights_data_coordinates_captures:
            # finds the knight with highest capture potential and removes it from the board
            key, _ = sorted(knights_data_coordinates_captures.items(), key=lambda x: (-x[1], x[0]))[0]
            knight_indexes.remove(key)
            matrix[key[0]][key[1]] = "0"
            count += 1
        else:
            break

    print(count)


if __name__ == "__main__":
    main()
