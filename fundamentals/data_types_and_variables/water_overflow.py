capacity = 255
pours = 0
for pour in range(int(input())):
    current_refill = int(input())
    pours += current_refill
    if capacity < pours:
        print("Insufficient capacity!")
        pours -= current_refill
    else:
        continue
else:
    print(pours)

