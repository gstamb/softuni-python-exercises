events = [x for x in input().split("|")]
coins = 100
energy = 100
for event in events:
    activity, value = event.split("-")
    value = int(value)
    if activity == "rest":
        new_energy_level = 0
        if energy + value > 100:
            new_energy_level = 100
        else:
            new_energy_level = energy + value
        energy_gained = new_energy_level - energy
        energy = new_energy_level
        print(f"You gained {energy_gained} energy.")
        print(f"Current energy: {energy}.")

    elif activity == "order":
        if energy - 30 >= 0:
            print(f"You earned {value} coins.")
            coins += value
            energy -= 30
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= value:
            print(f"You bought {activity}.")
            coins -= value
        else:
            print(f"Closed! Cannot afford {activity}.")
            break
else:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")



