initial_loot = input().split("|")

while True:
    instruction = input()

    if instruction == "Yohoho!":
        if initial_loot:
            len_loot = sum([len(x) for x in initial_loot])
            cnt = len(initial_loot)
            avg_loot = len_loot / cnt
            print(f"Average treasure gain: {avg_loot:.2f} pirate credits.")
        else:
            print("Failed treasure hunt.")

        break

    split = instruction.split()
    if instruction.startswith("Loot"):
        items = split[1:]
        for item in split[1:]:
            if item not in initial_loot:
                initial_loot.insert(0, item)

    elif instruction.startswith("Drop"):
        index = int(split[1])
        if 0 <= index <= len(initial_loot) - 1:
            item = initial_loot.pop(index)
            initial_loot.append(item)

    elif instruction.startswith("Steal"):
        length = int(split[1])
        stolen = initial_loot[-length:]
        initial_loot = [x for x in initial_loot if x not in stolen]
        print(", ".join(stolen))
