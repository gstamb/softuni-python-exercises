inventory = {}
temp = []

while True:

    mined = input()
    if mined == "stop":
        break

    temp.append(mined)

for item in range(0, len(temp), 2):
    key = temp[item]
    value = int(temp[item + 1])
    if key not in inventory:
        inventory[key] = value
    else:
        inventory[key] += value

for key, value in inventory.items():
    print(f"{key} -> {value}")
