def sort_list(nums: str) -> list:
    arr_nums = [int(x) for x in nums.split()]
    sorted_numbers = sorted(arr_nums)
    return sorted_numbers


input_nums = input()

print(sort_list(input_nums))
