string = input()
empty = ["", " "]
for index, char in enumerate(string):
    if char == ":":
        if index < len(string):
            if string[index + 1] not in empty:
                print(f"{char}{string[index + 1]}")
