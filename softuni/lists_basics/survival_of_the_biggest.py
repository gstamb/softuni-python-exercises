numbers = [int(x) for x in input().split()]
cnt_numbers_to_remove = int(input())
smallest = sorted(numbers)[:cnt_numbers_to_remove]

for number in smallest:
    numbers.remove(number)

print(", ".join(str(x) for x in numbers))



