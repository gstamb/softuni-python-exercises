list_of_numbers = [int(x) for x in input().split(", ")]

for item in range(len(list_of_numbers) - 1, -1, -1):
    if list_of_numbers[item] == 0:
        list_of_numbers.pop(item)
        list_of_numbers.append(0)

print(list_of_numbers)
