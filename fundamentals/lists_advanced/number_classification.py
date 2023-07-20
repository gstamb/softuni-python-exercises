import time
seq_nums = [int(x) for x in input().split(", ")]
# Approach using multiple list comprehensions
start_time = time.time()

sequence_numbers = seq_nums

positive_numbers = [str(x) for x in sequence_numbers if x >= 0]
negative_numbers = [str(x) for x in sequence_numbers if x < 0]
even_numbers = [str(x) for x in sequence_numbers if x % 2 == 0]
odd_numbers = [str(x) for x in sequence_numbers if x % 2 == 1]

end_time = time.time()
execution_time = end_time - start_time

print("Approach using multiple list comprehensions:")
print(f"Positive: {', '.join(positive_numbers)}")
print(f"Negative: {', '.join(negative_numbers)}")
print(f"Even: {', '.join(even_numbers)}")
print(f"Odd: {', '.join(odd_numbers)}")
print(f"Execution time: {execution_time} seconds\n")

# Approach using a single loop
start_time = time.time()

sequence_numbers = seq_nums

positive_numbers = []
negative_numbers = []
even_numbers = []
odd_numbers = []

for number in sequence_numbers:
    if number >= 0:
        positive_numbers.append(str(number))
    else:
        negative_numbers.append(str(number))

    if number % 2 == 0:
        even_numbers.append(str(number))
    else:
        odd_numbers.append(str(number))

end_time = time.time()
execution_time = end_time - start_time

print("Approach using a single loop:")
print(f"Positive: {', '.join(positive_numbers)}")
print(f"Negative: {', '.join(negative_numbers)}")
print(f"Even: {', '.join(even_numbers)}")
print(f"Odd: {', '.join(odd_numbers)}")
print(f"Execution time: {execution_time} seconds")


