disallowed = [".", ",", "_"]
for _ in range(int(input())):
    string = input()
    pure = all([x not in disallowed for x in string])
    if pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
