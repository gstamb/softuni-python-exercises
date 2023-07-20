towns = {}

while True:
    instruction = input()
    if instruction == "Sail":
        break
    town, population, gold = instruction.split("||")
    if town in towns:
        towns[town]["Population"] += int(population)
        towns[town]["Gold"] += int(gold)

    else:
        towns[town] = {"Population": int(population), "Gold": int(gold)}

while True:
    instruction = input()
    if instruction == "End":
        if towns:
            print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
            for town in towns:
                print(f"{town} -> Population: {towns[town]['Population']} citizens, Gold: {towns[town]['Gold']} kg")
        else:
            print("Ahoy, Captain! All targets have been plundered and destroyed!")
        break

    split = instruction.split("=>")
    if instruction.startswith("Plunder"):
        _, town, people, gold = split
        gold = int(gold)
        people = int(people)
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        towns[town]["Gold"] -= gold
        towns[town]["Population"] -= people
        if towns[town]["Gold"] <= 0 or towns[town]["Population"] <= 0:
            print(f"{town} has been wiped off the map!")
            del towns[town]

    elif instruction.startswith("Prosper"):
        _, town, gold = split
        if int(gold) >= 0:
            towns[town]["Gold"] += int(gold)
            print(f"{int(gold)} gold added to the city treasury. {town} now has {towns[town]['Gold']} gold.")
        else:
            print("Gold added cannot be a negative number!")
