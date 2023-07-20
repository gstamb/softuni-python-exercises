target_list = [int(x) for x in input().split()]
list_shot_targets = []
while True:
    instruction = input()
    if instruction == "End":
        break

    target = int(instruction)

    if target <= len(target_list) - 1:
        value = target_list[target]
        target_list = [x - value if x > value else x + value for x in target_list]
        list_shot_targets.append(target)

print(
    f"Shot targets: {len(list_shot_targets)} -> "
    f"{' '.join([str(-1) if index in list_shot_targets else str(x) for index, x in enumerate(target_list)])}")
