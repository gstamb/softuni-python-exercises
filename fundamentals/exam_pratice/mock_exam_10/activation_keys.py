activation_key = input()

while True:
    instruction = input()
    if instruction == "Generate":
        print(f"Your activation key is: {activation_key}")
        break
    split = instruction.split(">>>")
    if instruction.startswith("Contains"):
        _, substring = split
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif instruction.startswith("Flip"):
        _, case, start, end = split
        start = int(start)
        end = int(end)
        left = activation_key[:start]
        mid = "".join([x.lower() if case == "Lower" else x.upper() for x in activation_key[start:end]])
        right = activation_key[end:]
        activation_key = left + mid + right
        print(activation_key)
    elif instruction.startswith("Slice"):
        _, start, end = split
        start = int(start)
        end = int(end)

        left = activation_key[:start]
        right = activation_key[end:]
        activation_key = left + right

        print(activation_key)
