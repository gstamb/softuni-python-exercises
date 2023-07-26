from collections import deque


def main():
    """ Function receives two lists containing textiles and medications.
        Textiles is a queue consumed in FIFO order, while medication is a regular list consumed LIFO.
        The sum of textile and medication is used to craft safety items.

        The function will print a list of crafted items (in descending order of amount crafted and ascending order of name)
        and the remaining materials if any.
    """
    textiles = deque([int(x) for x in input().split()])
    medications = list([int(x) for x in input().split()])

    healing_item_table = {
        30: "Patch",
        40: "Bandage",
        100: "MedKit"
    }

    created_items = []

    while textiles and medications:
        textile = textiles.popleft()
        medication = medications.pop()
        healing_item = textile + medication

        if healing_item in healing_item_table:
            created_items.append(healing_item_table[healing_item])
        elif healing_item > 100:
            created_items.append("MedKit")
            remainder = healing_item - 100
            medications[-1] += remainder
        else:
            medication += 10
            medications.append(medication)

    if not textiles and not medications:
        print("Textiles and medicaments are both empty.")
    elif not textiles:
        print("Textiles are empty.")
    elif not medications:
        print("Medicaments are empty.")

    counted = {item: created_items.count(item) for item in created_items}
    for key, value in sorted(counted.items(), key=lambda x: (-x[1], x[0])):
        print(f"{key} - {value}")

    if medications:
        print(f"Medicaments left: {', '.join([str(x) for x in medications[::-1]])}")
    if textiles:
        print(f"Textiles left: {', '.join([str(x) for x in textiles])}")


if __name__ == "__main__":
    main()
