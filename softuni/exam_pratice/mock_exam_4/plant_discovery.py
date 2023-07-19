plants = {}
for _ in range(int(input())):
    plant, rarity = input().split("<->")
    if plant not in plants:
        plants[plant] = {"Rarity": int(rarity), "Rating": []}
    else:
        plants[plant]["Rarity"] = int(rarity)

while True:
    instruction = input()
    if instruction == "Exhibition":
        break

    if instruction.startswith("Rate"):
        _, plant, _, rating = instruction.split()
        if plant in plants:
            plants[plant]["Rating"].append(int(rating))
        else:
            print("error")
    elif instruction.startswith("Update"):
        _, plant, _, rarity = instruction.split()
        if plant in plants:
            plants[plant]["Rarity"] = int(rarity)
        else:
            print("error")
    elif instruction.startswith("Reset"):
        _, plant = instruction.split()
        if plant in plants:
            plants[plant]["Rating"].clear()
        else:
            print("error")

print("Plants for the exhibition:")
for plant, data in plants.items():
    if len(data["Rating"]) > 0:
        print(f"- {plant}; Rarity: {data['Rarity']}; Rating: {sum(data['Rating']) / len(data['Rating']):.2f}")
    else:
        print(f"- {plant}; Rarity: {data['Rarity']}; Rating: 0.00")
