string = input()
list_of_chars = [x for x in string]
last_char = ""

for index, char in enumerate(list_of_chars):
    if last_char == char:
        list_of_chars[index] = ""
    else:
        last_char = char

print("".join(x for x in list_of_chars if x != ""))