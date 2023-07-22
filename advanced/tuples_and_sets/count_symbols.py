def main():
    string = input()
    word_count = {}
    for char in string:
        word_count[char] = word_count.get(char, 0) + 1

    [print(f"{char}: {count} time/s") for char, count in sorted(word_count.items())]


if __name__ == "__main__":
    main()
