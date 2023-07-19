raw_string = input()

while True:

    instruction = input()
    if instruction == "Done":
        break

    if instruction.startswith("Take"):
        raw_string = "".join([x for index, x in enumerate(raw_string) if index % 2 == 1])
        print(raw_string)
    elif instruction.startswith("Cut"):
        _, index, length = instruction.split()
        string = raw_string[int(index):int(index) + int(length)]
        raw_string = raw_string.replace(string, "", 1)
        print(raw_string)
    elif instruction.startswith("Substitute"):
        _, old, new = instruction.split()
        if old in raw_string:
            raw_string = raw_string.replace(old, new)
            print(raw_string)
        else:
            print("Nothing to replace!")

print(f"Your password is: {raw_string}")