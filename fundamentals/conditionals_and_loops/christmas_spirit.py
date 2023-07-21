decorations_cnt = int(input())
days_2christmas = int(input())
extra = 0

total_cost = 0
total_spirit = 0

ornament_set = (2, 5)
tree_skirt = (5, 3)
tree_garland = (3, 10)
tree_lights = (15, 17)

for day in range(1, days_2christmas + 1):
    if day % 11 == 0:
        extra += 2

    if day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt[0]
        total_cost += tree_garland[0]
        total_cost += tree_lights[0]
        if day == days_2christmas:
            total_spirit -= 30

    if day % 5 == 0:
        total_cost += tree_lights[0] * (decorations_cnt + extra)

        total_spirit += tree_lights[1]

    if day % 15 == 0:
        # bonus spirit
        total_spirit += 30

    if day % 3 == 0:
        total_cost += tree_skirt[0] * (decorations_cnt + extra)
        total_cost += tree_garland[0] * (decorations_cnt + extra)

        total_spirit += tree_skirt[1]
        total_spirit += tree_garland[1]

    if day % 2 == 0:
        total_cost += ornament_set[0] * (decorations_cnt + extra)
        total_spirit += ornament_set[1]

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
