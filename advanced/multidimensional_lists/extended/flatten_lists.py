def main():
    """Returns a flattened list out of a matrix input as a string"""
    list_as_str = input().split("|")

    # Remove any empty elements and strip leading/trailing whitespaces from each sublist
    sublist = [x.strip() for x in list_as_str if x != ""]

    # Create a matrix from the sublists, parsing each element as an integer
    # The matrix is formed in reverse order to match the user's input sequence
    matrix = [[int(x) for x in y.split()] for y in reversed(sublist)]
    # matrix = [[int(x) for x in y.split()] for y in reversed([x.strip() for x in input().split("|") if x != ""])]

    # Flatten the matrix into a 1-dimensional list of integers as strings
    flattened_matrix = [str(element) for sublist in matrix for element in sublist]

    # Print the result as a space-separated string
    print(" ".join(flattened_matrix))


if __name__ == "__main__":
    main()
