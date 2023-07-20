pirate_ship = [int(x) for x in input().split(">")]
battle_ship = [int(x) for x in input().split(">")]
max_section_health = int(input())
flag = False
while True:

    instruction = input()
    if instruction == "Retire":
        print(f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(battle_ship)}")
        break

    split = instruction.split()

    if instruction.startswith("Fire"):
        index = int(split[1])
        damage = int(split[2])
        if 0 <= index <= len(battle_ship) - 1:
            battle_ship[index] -= damage
            if battle_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                break

    elif instruction.startswith("Defend"):
        start_index = int(split[1])
        end_index = int(split[2])
        damage = int(split[3])
        if 0 <= start_index <= len(pirate_ship) - 1 and 0 <= end_index <= len(pirate_ship) - 1:
            for section in range(start_index, end_index + 1):
                pirate_ship[section] -= damage
                if pirate_ship[section] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    flag = True
                    break

        if flag:
            break

    elif instruction.startswith("Repair"):
        index = int(split[1])
        health = int(split[2])

        if 0 <= index <= len(pirate_ship) - 1:
            start = pirate_ship[index]
            if pirate_ship[index] + health > max_section_health:
                pirate_ship[index] = max_section_health
            else:
                pirate_ship[index] += health

    elif instruction.startswith("Status"):
        print(f"{len([x for x in pirate_ship if x < max_section_health * 0.2])} sections need repair.")
