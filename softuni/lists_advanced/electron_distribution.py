number = int(input())
result = []
i = 0

while 0 < number:
    i += 1
    electron = 2 * (i ** 2)

    if number > electron:
        result.append(electron)
        number -= electron

    else:
        result.append(number)
        number = 0

print(result)
