string = input()
unique = []

start_index = 0
result = ""
for index, symbol in enumerate(string):
    if symbol.upper() not in unique and not symbol.isdigit():
        unique.append(symbol.upper())

    if symbol.isdigit():
        if index + 1 < len(string):
            next_symbol = string[index + 1]
            if next_symbol.isdigit():
                symbol = string[index] + string[index + 1]

        repeat = int(symbol)
        result += string[start_index:index].upper() * repeat
        start_index = index + 1

print(f"Unique symbols used: {len(unique)}")
if not result:
    print(string.upper())
else:
    print(result)


