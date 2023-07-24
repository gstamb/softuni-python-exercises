def main():
    """ Generates a matrix of palindromes """
    rows, columns = map(int, input().split())

    # ascii a-z = 97 - 122 inclusive

    for row in range(rows):
        for column in range(columns):
            palindrome = chr(row + 97) + chr(column + row + 97) + chr(row + 97)
            print(palindrome, end=" ")

        print()


if __name__ == "__main__":
    main()
