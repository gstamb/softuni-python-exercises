def is_palindrome(num: str) -> bool:
    backwards = num[::-1]
    return True if num == backwards else False


input_nums = [x for x in input().split(", ")]

for number in input_nums:
    print(is_palindrome(number))
