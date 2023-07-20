input_message = input()

while True:

    instruction = input()
    if instruction == "Reveal":
        break

    if instruction.startswith("Insert"):
        index = int(instruction.split(":|:")[1])
        left = input_message[:index]
        right = input_message[index:]
        input_message = left + " " + right
        print(input_message)

    elif instruction.startswith("Reverse"):
        _, substring = instruction.split(":|:")
        if substring in input_message:
            index = input_message.index(substring)
            left = input_message[:index]
            right = input_message[index + len(substring):]
            input_message = left + right + substring[::-1]
            print(input_message)
        else:
            print("error")
    elif instruction.startswith("Change"):
        _, old, new = instruction.split(':|:')
        input_message = input_message.replace(old, new)
        print(input_message)

print(f"You have a new text message: {input_message}")
