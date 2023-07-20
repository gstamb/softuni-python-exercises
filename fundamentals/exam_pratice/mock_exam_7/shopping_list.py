groceries = input().split("!")

while True:

    instruction = input()
    if instruction == "Go Shopping!":
        break

    if instruction.startswith("Urgent"):
        _, product = instruction.split()
        if product in groceries:
            pass
        else:
            groceries.insert(0, product)
    elif instruction.startswith("Unnecessary"):
        _, product = instruction.split()
        if product in groceries:
            groceries.remove(product)
    elif instruction.startswith("Correct"):
        _, old, new = instruction.split()
        if old in groceries:
            groceries[groceries.index(old)] = new
    elif instruction.startswith("Rearrange"):
        _, product = instruction.split()
        if product in groceries:
            groceries.remove(product)
            groceries.append(product)
print(", ".join(groceries))
