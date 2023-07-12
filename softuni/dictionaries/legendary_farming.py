def ingest_items(items: list) -> None:
    for item in range(0, len(items), 2):
        value = int(items[item])
        key = items[item + 1]
        if key in inventory.keys():
            inventory[key] += value
            if check_if_found():
                return True
        else:
            if key in junk.keys():
                junk[key] += value
            else:
                junk[key] = value


def check_if_found():
    for name, value in legendary_items.items():
        materials = value[0]
        quantity = value[1]
        if materials in inventory.keys():
            if inventory[materials] >= quantity:
                print(f"{name} obtained!")
                inventory[materials] -= quantity
                return True
    else:
        return False


legendary_items = {"Shadowmourne": ("shards", 250),
                   "Valanyr": ("fragments", 250),
                   "Dragonwrath": ("motes", 250)
                   }
inventory = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

junk = {

}
found = False
while not found:
    list_materials = input()
    found = ingest_items([x.lower() for x in list_materials.split()])

for material, quantity in inventory.items():
    print(f"{material}: {quantity}")

for material, quantity in junk.items():
    print(f"{material}: {quantity}")
