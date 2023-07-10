def sum_odd_even(string: str) -> str:
    sum_of_odd_digits = sum([int(x) for x in string if int(x) % 2 == 1])
    sum_of_even_digits = sum([int(x) for x in string if int(x) % 2 == 0])

    string = f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
    return string


input_string = input()
print(sum_odd_even(input_string))
