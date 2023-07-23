def perform_action(action: str, set_first: set, set_second: set):
    if action.startswith("Add First"):
        add_elements = map(int, action.split()[2:])
        set_first.update(add_elements)
    elif action.startswith("Add Second"):
        add_elements = map(int, action.split()[2:])
        set_second.update(add_elements)
    elif action.startswith("Remove First"):
        remove_elements = map(int, action.split()[2:])
        set_first.difference_update(remove_elements)

    elif action.startswith("Remove Second"):
        remove_elements = map(int, action.split()[2:])
        set_second.difference_update(remove_elements)

    elif action.startswith("Check"):
        if set_first.issubset(set_second) or set_second.issubset(set_first):
            print(True)
        else:
            print(False)


def main():
    first_seq = set(map(int, input().split()))
    second_seq = set(map(int, input().split()))

    for _ in range(int(input())):
        instruction = input()
        perform_action(instruction, first_seq, second_seq)

    else:
        print(', '.join(map(str, sorted(first_seq))))
        print(', '.join(map(str, sorted(second_seq))))


if __name__ == "__main__":
    main()
