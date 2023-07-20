health = 100
coins = 0
rooms = input().split("|")

for room in rooms:
    split = room.split()
    if room.startswith("potion"):
        _, amount = split
        start = health
        if health + int(amount) > 100:
            health = 100
        else:
            health += int(amount)
        print(f"You healed for {health - start} hp.")
        print(f"Current health: {health} hp.")
    elif room.startswith("chest"):
        _, amount = split
        print(f"You found {amount} bitcoins.")
        coins += int(amount)
    else:
        monster, damage = split
        damage = int(damage)
        if health - damage > 0:
            print(f"You slayed {monster}.")
            health -= damage
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {rooms.index(room)+1}")
            break
else:
    print(f"You've made it!")
    print(f"Bitcoins: {coins}")
    print(f"Health: {health}")
