def sum_numbers(nums: list) -> int:
    result = sum(nums[:2])
    last_item = nums[2]
    return subtract(result, last_item)


def subtract(sum_nums: int, third_integer: int) -> int:
    result = sum_nums - third_integer
    return result


numbers = [int(input()) for x in range(3)]
print(sum_numbers(numbers))
