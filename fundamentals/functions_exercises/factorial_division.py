def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


first_num = int(input())
second_num = int(input())
factorial_first = factorial(first_num)
factorial_second = factorial(second_num)

result = factorial_first / factorial_second
print(f"{result:.2f}")
