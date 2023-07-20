def even_number(num):
    return True if num % 2 == 0 else False


input_numbers = [int(x) for x in input().split()]
result = filter(even_number, input_numbers)
print(list(result))