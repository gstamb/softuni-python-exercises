elements = input().split()
cnt = 0
player_a = []
player_b = []
while True:
    cnt += 1
    move = input()
    if move == "end":
        if len(elements) > 0:
            print("Sorry you lose :(")
            print(f"{' '.join(elements)}")
        break

    x, y = map(int, move.split())

    if x > len(elements)-1 or y > len(elements)-1 or x < 0 or y < 0 or x == y:
        mid = len(elements) // 2
        elements.insert(mid, f"-{cnt}{'a'}")
        elements.insert(mid, f"-{cnt}{'a'}")
        print("Invalid input! Adding additional elements to the board")
        continue

    if elements[x] == elements[y]:
        print(f"Congrats! You have found matching elements - {elements[x]}!")
        if x > y:
            elements.pop(x)
            elements.pop(y)
        elif y > x:
            elements.pop(y)
            elements.pop(x)

        if len(elements) == 0:
            print(f"You have won in {cnt} turns!")
            break

    else:
        print(f"Try again!")
