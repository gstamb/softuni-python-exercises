input_list = [int(x) for x in input().split()]


def min_max_index(cmnd):
    even_or_odd = cmnd.split()[1]
    min_or_max = cmnd.split()[0]
    if even_or_odd == "even":
        even_elements = [x for x in input_list if x % 2 == 0]
        if even_elements:
            if min_or_max == "max":
                position = len(input_list) - 1 - input_list[::-1].index(max(even_elements))
                print(position)
            else:
                position = len(input_list) - 1 - input_list[::-1].index(min(even_elements))
                print(position)
        else:
            print("No matches")
    else:
        odd_elements = [x for x in input_list if x % 2 == 1]
        if odd_elements:
            if min_or_max == "max":
                position = len(input_list) - 1 - input_list[::-1].index(max(odd_elements))
                print(position)
            else:
                position = len(input_list) - 1 - input_list[::-1].index(min(odd_elements))
                print(position)
        else:
            print("No matches")


def first_or_last(cmnd):
    even_or_odd = cmnd.split()[2]
    cnt = int(cmnd.split()[1])
    first_last = cmnd.split()[0]
    if cnt > len(input_list):
        print("Invalid count")
    else:
        if even_or_odd == "even":
            even_elements = [x for x in input_list if x % 2 == 0]
            if even_elements:
                if cnt > len(even_elements):
                    print(even_elements)
                else:
                    if first_last == "first":
                        print(even_elements[:cnt])
                    else:
                        print(even_elements[-cnt:])
            else:
                print([])
        else:
            odd_elements = [x for x in input_list if x % 2 == 1]
            if odd_elements:
                if cnt > len(odd_elements):
                    print(odd_elements)
                else:
                    if first_last == "first":
                        print(odd_elements[:cnt])
                    else:
                        print(odd_elements[-cnt:])
            else:
                print([])


while True:
    command = input()
    if command == "end":
        break
    elif command.startswith("exchange"):
        index = int(command.split()[1])
        if 0 <= index < len(input_list):
            left = input_list[index + 1:]
            right = input_list[:index + 1]
            input_list = left + right
        else:
            print("Invalid index")
    elif command.startswith("max"):
        min_max_index(command)

    elif command.startswith("min"):
        min_max_index(command)

    elif command.startswith("first"):
        first_or_last(command)
    elif command.startswith("last"):
        first_or_last(command)
print(input_list)
