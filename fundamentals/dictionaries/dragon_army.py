from statistics import mean

dragons = {}

for dragon in range(int(input())):
    dragon_type, name, damage, health, armor = input().split()
    if damage == "null":
        damage = 45
    if health == "null":
        health = 250
    if armor == "null":
        armor = 10

    if dragon_type not in dragons:
        dragons[dragon_type] = {name: {"damage": int(damage), "health": int(health), "armor": int(armor)}}

    else:
        if name in dragons[dragon_type]:
            dragons[dragon_type][name] = {"damage": int(damage), "health": int(health), "armor": int(armor)}
        else:
            dragons[dragon_type][name] = {"damage": int(damage), "health": int(health), "armor": int(armor)}

for key, value in dragons.items():
    print(
        f"{key}::({mean([y['damage'] for y in [x for x in value.values()]]):.2f}/{mean([y['health'] for y in [x for x in value.values()]]):.2f}/{mean([y['armor'] for y in [x for x in value.values()]]):.2f})")
    for subkey, subvalue in sorted(value.items(), key=lambda x: x[0]):
        print(f"-{subkey} -> damage: {subvalue['damage']}, health: {subvalue['health']}, armor: {subvalue['armor']}")
