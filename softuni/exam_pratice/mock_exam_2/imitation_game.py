base_message = input()
while True:

    instruction = input()
    if instruction == "Decode":
        break

    if instruction.startswith("Change"):
        _, letter, replacement = instruction.split("|")
        base_message = base_message.replace(letter, replacement)
    elif instruction.startswith("Insert"):
        _, index, letter = instruction.split("|")
        inserted = [x for x in base_message]
        inserted.insert(int(index), letter)
        base_message = "".join(inserted)
    elif instruction.startswith("Move"):
        _, elements = instruction.split("|")
        left = base_message[:int(elements)]
        right = base_message[int(elements):]
        base_message = right + left

print(f"The decrypted message is: {base_message}")
