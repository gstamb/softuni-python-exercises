array_integers = [int(x) for x in input().split()]


def swap(index_1, index_2):
    array_integers[index_1], array_integers[index_2] = array_integers[index_2], array_integers[index_1]


def multiply(index_1, index_2):
    array_integers[index_1] = array_integers[index_1] * array_integers[index_2]


while True:
    instruction = input()
    if instruction == "end":
        break

    if instruction.startswith("swap"):
        _, index_first, index_second = instruction.split()
        swap(int(index_first), int(index_second))
    elif instruction.startswith("multiply"):
        _, index_first, index_second = instruction.split()
        multiply(int(index_first), int(index_second))
    elif instruction.startswith("decrease"):
        array_integers = [x - 1 for x in array_integers]

print(", ".join(str(x) for x in array_integers))
