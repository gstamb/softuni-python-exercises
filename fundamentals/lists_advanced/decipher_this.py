decipher_string = input().split()

for word in decipher_string:
    chars = [x for x in word if x.isalpha()]
    digits = int("".join([x for x in word if x.isdigit()]))
    chars[0], chars[-1] = chars[-1], chars[0]
    char = chr(digits)
    string = "".join(chars)

    print(char + string, end=" ")
