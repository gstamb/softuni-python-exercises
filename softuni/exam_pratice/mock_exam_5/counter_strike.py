initial_energy = int(input())

battles_won = 0
while True:
    instruction = input()

    if instruction == "End of battle":
        print(f"Won battles: {battles_won}. Energy left: {initial_energy}")
        break

    battle = int(instruction)

    if initial_energy - battle >= 0:
        initial_energy -= battle
        battles_won += 1
        if battles_won % 3 == 0:
            initial_energy += battles_won
    else:
        print("Not enough energy!", end=" ")
        print(f"Game ends with {battles_won} won battles and {initial_energy} energy")
        break

