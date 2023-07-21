from collections import deque


def reverse_string(string: str):
    queue_chars = deque(string.split())
    reversed_string = ""
    while queue_chars:
        reversed_string += queue_chars.pop() + " "

    return reversed_string.strip()


def main():
    str_to_reverse = input()
    print(reverse_string(str_to_reverse))


if __name__ == "__main__":
    main()
