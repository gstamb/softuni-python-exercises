def merge(instructions):
    index_start = int(instructions.split()[1])
    index_end = int(instructions.split()[2]) + 1
    if len(input_data) - 1 > index_end:
        index_end = len(input_data) - 1

    # assigns range of a list to a range to a single value , effectively shortening it
    input_data[index_start: index_end] = [''.join(input_data[index_start: index_end])]


def divide(instructions):
    index_start = int(instructions.split()[1])
    partitions = int(instructions.split()[2])

    # shortens the target string until it can be evenly divided
    rest = ""
    if len(input_data[index_start]) % partitions != 0:
        while len(input_data[index_start]) % partitions != 0:
            rest += input_data[index_start][-1]
            input_data[index_start] = input_data[index_start][:-1]

    x = input_data[index_start]

    chunks, chunk_size = len(x), len(x) // partitions
    split = [x[i:i + chunk_size] for i in range(0, chunks, chunk_size)]
    input_data.pop(index_start)
    for index, item in enumerate(split[::-1]):
        if index == 0:
            item += rest
        input_data.insert(index_start, item)


input_data = input().split()

while True:
    action = input()
    if action == "3:1":
        break
    elif action.startswith("merge"):
        merge(action)

    elif action.startswith("divide"):
        divide(action)

input_data = [x for x in input_data if x != ""]

print(" ".join(input_data))
