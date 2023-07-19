string = [int(x) for x in input().split("@")]
landing_pos = 0
while True:
    instruction = input()
    if instruction == "Love!":
        break

    index = int(instruction.split()[1])
    if landing_pos + index > len(string) - 1:
        landing_pos = 0
    else:
        landing_pos = landing_pos + index
    if string[landing_pos] == 0:
        print(f"Place {landing_pos} already had Valentine's day.")
    else:
        string[landing_pos] -= 2
        if string[landing_pos] <= 0:
            string[landing_pos] = 0
            print(f"Place {landing_pos} has Valentine's day.")

print(f"Cupid's last position was {landing_pos}.")
if sum(string) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len([x for x in string if x != 0])} places.")
