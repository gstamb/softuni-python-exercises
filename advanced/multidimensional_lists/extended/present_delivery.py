def find_santa_location(board):
    """Finds Santa's location in the matrix.

    Args:
        board (list[list[str]]): The matrix representing the neighborhood.

    Returns:
        tuple: A tuple containing the row and column indices of Santa's location.
    """
    for row, columns in enumerate(board):
        for column, symbol in enumerate(columns):
            if symbol == "S":
                return row, column


def find_cnt_nice_kids(board):
    """Finds the count of nice kids in the matrix.

    Args:
        board (list[list[str]]): The matrix representing the neighborhood.

    Returns:
        int: The count of nice kids in the neighborhood.
    """
    return sum([1 for row, columns in enumerate(board) for column, symbol in enumerate(columns) if symbol == "V"])


def move_santa(board, direction, presents):
    """Moves Santa to a new location based on the provided direction.

    Args:
        board (list[list[str]]): The matrix representing the neighborhood.
        direction (str): The direction to move Santa (up, down, left, or right).
        presents (list[int]): A list to track the number of presents delivered.

    Modifies:
        board: Updates the board after Santa's move.
        presents: Appends the number of presents delivered based on Santa's action.
    """
    # coordinates of Santa's moves by direction in addition to current location
    possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, +1)}

    current_x, current_y = find_santa_location(board)

    new_x = current_x + possible_moves[direction][0]
    new_y = current_y + possible_moves[direction][1]

    # validate new location
    if 0 <= new_x < len(board) and 0 <= new_y < len(board):
        # deliver a present if Santa visits a nice kid
        if board[new_x][new_y] == "V":
            board[new_x][new_y] = "S"
            board[current_x][current_y] = "-"
            presents.append(1)
        # no present if Santa visits a naughty kid
        elif board[new_x][new_y] == "X":
            board[new_x][new_y] = "S"
            board[current_x][current_y] = "-"
        # deliver presents to all nearby kids if Santa geta cookie
        elif board[new_x][new_y] == "C":
            board[new_x][new_y] = "S"
            board[current_x][current_y] = "-"
            deliver_present_nearby(board, presents)
        else:
            board[new_x][new_y] = "S"
            board[current_x][current_y] = "-"


def deliver_present_nearby(board, presents):
    """Delivers presents to all nearby kids when Santa gets a cookie.

    Args:
        board (list[list[str]]): The matrix representing the neighborhood.
        presents (list[int]): A list to track the number of presents delivered.

    Modifies:
        board: Updates the board by removing the delivered presents.
        presents: Appends the number of presents delivered based on Santa's action.
    """

    # refine possible moves for Santa in each direction
    possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, +1)}

    current_x, current_y = find_santa_location(board)

    # check if the new location is within the boundaries of the board
    for direction, val in possible_moves.items():
        new_x = current_x + val[0]
        new_y = current_y + val[1]
        if 0 <= new_x < len(board) and 0 <= new_y < len(board):
            # deliver presents of all nearby kids
            if board[new_x][new_y] == "V":
                board[new_x][new_y] = "-"
                presents.append(1)
            elif board[new_x][new_y] == "X":
                board[new_x][new_y] = "-"
                presents.append(2)


def main():
    """Plays the Santa delivery game.

        The game involves Santa delivering presents to kids in the neighborhood.
        Santa can move in four directions (up, down, left, or right) and deliver presents to nice kids ('V').
        If Santa gets a cookie ('C'), he delivers presents to all nearby kids.
        If Santa visits a naughty kid ('X'), no presents are delivered.

        The game continues until Santa runs out of presents, or it becomes Christmas morning.

        Input:
        - The number of presents to be delivered (deliver_presents_cnt).
        - The size of the neighborhood (neighbourhood_size).
        - The matrix representing the neighborhood (matrix).
        - Instructions to move Santa or end the game.

        Output:
        - The updated matrix after Santa's actions.
        - The number of nice kids who received a present or missed a present.

        Note:
        - The matrix is represented as a list of lists of strings.
        - The characters used in the matrix are 'S' (Santa), 'V' (nice kid), 'X' (naughty kid), 'C' (cookie), and '-' (empty).
        - If all nice kids receive a present, Santa is praised; otherwise, he's informed about the number of nice kids who missed a present.
        - If Santa runs out of presents before delivering to all nice kids, he is informed about it.
        """
    # read the number of presents to be delivered
    deliver_presents_cnt = int(input())

    # read the size of the neighborhood and create the matrix
    neighbourhood_size = int(input())

    matrix = [[x for x in input().split()] for _ in range(neighbourhood_size)]

    delivered_presents = []
    # santa will keep receiving instructions until he runs out of presents, or it becomes Christmas
    while sum(delivered_presents) < deliver_presents_cnt:
        instruction = input()
        if instruction == "Christmas morning":
            break

        move_santa(matrix, instruction, delivered_presents)

    count_nice_kids = find_cnt_nice_kids(matrix)

    # count presents delivered any kid regardless nice or not
    if sum([1 for _ in delivered_presents]) == deliver_presents_cnt and count_nice_kids:
        print("Santa ran out of presents!")
    # print the current state of the matrix
    [print(" ".join(x)) for x in matrix]

    if count_nice_kids:
        print(f"No presents for {count_nice_kids} nice kid/s.")
    else:
        # list comprehension sorts only presents delivered to nice kids
        print(f"Good job, Santa! {sum([x for x in delivered_presents if x == 1])} happy nice kid/s.")


if __name__ == "__main__":
    main()
