starting_string = input()

while True:

    instruction = input()
    if instruction == "Travel":
        break

    if instruction.startswith("Add"):
        _, index, string = instruction.split(":")
        index = int(index)
        if len(starting_string) - 1 >= int(index):
            left = starting_string[:index]
            right = starting_string[index:]
            starting_string = left + string + right
        print(starting_string)

    elif instruction.startswith("Remove"):
        _, start, stop = instruction.split(":")
        start = int(start)
        stop = int(stop) + 1
        if len(starting_string) - 1 >= start and len(starting_string) >= stop:
            replaced = [x for x in starting_string]
            replaced[start: stop] = ""
            starting_string = "".join(replaced)
        print(starting_string)
    elif instruction.startswith("Switch"):
        _, old, new = instruction.split(":")
        if old in starting_string:
            starting_string = starting_string.replace(old, new)
        print(starting_string)

print(f"Ready for world tour! Planned stops: {starting_string}")

