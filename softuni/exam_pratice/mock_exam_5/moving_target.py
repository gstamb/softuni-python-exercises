initial_targets = [int(x) for x in input().split()]


def get_values(command: str):
    _, first, second = command.split()
    first, second = int(first), int(second)
    return first, second


def validate_index(indx):
    if 0 <= indx <= len(initial_targets) - 1:
        return True
    else:
        return False


while True:
    instruction = input()
    if instruction == "End":
        print("|".join(str(x) for x in initial_targets))
        break

    if instruction.startswith("Shoot"):
        index, power = get_values(instruction)
        if validate_index(index):
            initial_targets[index] -= power
            if initial_targets[index] <= 0:
                initial_targets.pop(index)
    elif instruction.startswith("Add"):
        index, value = get_values(instruction)
        if validate_index(index):
            initial_targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif instruction.startswith("Strike"):
        index, radius = get_values(instruction)
        if index - radius >= 0 and index + radius + 1 <= len(initial_targets) - 1:
            initial_targets[index - radius:index + radius + 1] = ""
        else:
            print("Strike missed!")
