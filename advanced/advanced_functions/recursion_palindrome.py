def palindrome(word: str, index=0):
    """ Receives a word and recursively checks if it is a palindrome """
    first_index = index
    last_index = len(word) - 1 - index
    if word[first_index] == word[last_index]:
        if index <= (len(word) - 1) // 2:
            return palindrome(word, index + 1)
        else:
            return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"


def main():
    print(palindrome("peter", 0))


if __name__ == "__main__":
    main()
