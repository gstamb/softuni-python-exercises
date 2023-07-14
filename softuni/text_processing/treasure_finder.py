import re

cypher = [int(x) for x in input().split()]

while True:
    message = input()
    if message == "find":
        break

    decrypted = ""
    for index, char in enumerate(message):
        target = index % len(cypher)
        decrypted += chr(ord(char) - cypher[target])

    pattern = "(?<=&)(.*?)(?=&)"
    m = re.search(pattern, decrypted)
    material = m.group(1)

    pattern = "(?<=<)(.*?)(?=>)"
    m = re.search(pattern, decrypted)
    location = m.group(1)

    print(f"Found {material} at {location}")
