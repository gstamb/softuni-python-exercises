seq_numbers = [int(x) for x in input().split()]

sum_captured = 0
while seq_numbers:
    index = int(input())

    if index < 0:
        removed = seq_numbers.pop(0)
        sum_captured += removed
        seq_numbers.append(seq_numbers[-1])
        seq_numbers = [x + removed if x <= removed else x - removed for x in seq_numbers]
    elif index > len(seq_numbers) - 1:
        removed = seq_numbers.pop()
        sum_captured += removed
        seq_numbers.append(seq_numbers[0])
        seq_numbers = [x + removed if x <= removed else x - removed for x in seq_numbers]

    else:
        removed = seq_numbers.pop(index)
        sum_captured += removed
        # increment/decrement values depending on removed
        seq_numbers = [x + removed if x <= removed else x - removed for x in seq_numbers]

print(sum_captured)

