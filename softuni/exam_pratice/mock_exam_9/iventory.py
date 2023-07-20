collection = input().split(", ")

while True:

    instruction = input()
    if instruction == "Craft!":
        break

    split = instruction.split(" - ")
    if instruction.startswith("Collect"):
        item = split[1]
        if item not in collection:
            collection.append(item)
    elif instruction.startswith("Drop"):
        item = split[1]
        if item in collection:
            collection.remove(item)
    elif instruction.startswith("Renew"):
        item = split[1]
        if item in collection:
            collection.remove(item)
            collection.append(item)
    elif instruction.startswith("Combine"):
        old, new = split[1].split(":")
        if old in collection:
            index = collection.index(old)
            collection.insert(index+1, new)
print(", ".join(collection))
