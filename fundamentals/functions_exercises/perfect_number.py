def is_perfect(num: int) -> bool:
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)

    if sum(divisors) == num:
        return True
    else:
        return False


target_num = int(input())

if is_perfect(target_num):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
