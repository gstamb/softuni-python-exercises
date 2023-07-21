from collections import deque


def check_matching_brackets(brackets):
    # create a queue to hold opening brackets
    queue = deque()
    left = ["{", "[", "("]
    right = ["}", "]", ")"]

    for index, item in enumerate(brackets):
        if item in left:
            queue.append(left.index(item))
        elif item in right:
            right_index = right.index(item)
            if queue:
                if right_index == queue.pop():
                    continue
                else:
                    return "NO"

            else:
                return "NO"

    else:
        return "YES"


def main():
    string_to_check = input()
    brackets = [x for x in string_to_check]

    print(check_matching_brackets(brackets))


if __name__ == "__main__":
    main()
