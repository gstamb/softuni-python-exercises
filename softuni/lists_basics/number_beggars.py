earned = [int(x) for x in input().split(", ")]
number = int(input())
result = []

if len(earned) == number:
    pass
elif number == 1:
    sum = sum(earned)
    earned = [sum]
elif len(earned) < number:
    while len(earned) < number:
        earned.append(0)
else:
    while len(earned) % number != 0:
        earned.append(0)

    temp = []
    for x in range(len(earned)):
        temp.append(earned[x])
        if len(temp) == number:
            result.append(temp)
            temp = []

    earned = [sum(x) for x in zip(*result)]
print(earned)
