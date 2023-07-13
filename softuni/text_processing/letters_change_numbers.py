def get_pos(letter: str) -> int:
    return ord(letter.lower()) - 96


def add_next(following_char, temp):
    position = get_pos(next_char)
    if following_char.isupper():
        return temp - position
    elif following_char.islower():
        return temp + position


input_string = input().split()

result = 0
for index, substring in enumerate(input_string):
    number = int(substring[1:-1])
    previous = substring[0]
    next_char = substring[-1]

    position_in_alphabet_previous = get_pos(previous)

    if previous.isupper():
        temporary = number / position_in_alphabet_previous
        result += add_next(next_char, temporary)
    elif previous.islower():
        temporary = number * position_in_alphabet_previous
        result += add_next(next_char, temporary)


print(f"{result:.2f}")
