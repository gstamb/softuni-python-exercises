def min_max_sum(string: str) -> list:
    arr = [int(x) for x in string.split()]
    min_num = min(arr)
    max_num = max(arr)
    sum_of_nums = sum(arr)

    return (min_num, max_num, sum_of_nums)


input_string = input()
minimum_number, maximum_number, sum_of_numbers = min_max_sum(input_string)
print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_numbers}")
