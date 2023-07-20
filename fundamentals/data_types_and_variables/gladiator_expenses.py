lost_fights_count = int(input())
helmet_cost = float(input())
sword_cost = float(input())
shield_cost = float(input())
armor_cost = float(input())

cost = 0
shield_cnt = 0
trashed_helmed = 0
for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0 and fight % 3 == 0:
        cost += shield_cost
        shield_cnt += 1
        if shield_cnt % 2 == 0:
            cost += armor_cost

    if fight % 3 == 0:
        cost += sword_cost
    if fight % 2 == 0:
        cost += helmet_cost


print(f"Gladiator expenses: {cost:.2f} aureus")
