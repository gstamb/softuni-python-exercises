from collections import Counter

dwarfs = {}

while True:
    entry = input()
    if entry == "Once upon a time":
        break

    name, color, physics = entry.split(" <:> ")
    key = f"{name} - {color}"
    value = int(physics)

    if key in dwarfs:
        old_val = dwarfs[key]
        if old_val < value:
            dwarfs[key] = value
    else:
        dwarfs[key] = value


sorted_dwarfs = sorted(dwarfs.items(), key=lambda x: (-x[1], -Counter([dwarf.split(" - ")[1] for dwarf in dwarfs.keys()]).get(x[0].split(" - ")[1], 0)))

for dwarf, psy in sorted_dwarfs:
    name, color = dwarf.split(" - ")
    print(f"({color}) {name} <-> {psy}")
