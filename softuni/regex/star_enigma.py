import re

data = {"attacked": [], "destroyed": []}
for messages in range(int(input())):
    message = input()

    pattern = "([starSTAR])+?"
    m = re.findall(pattern, message)

    key = len(m)
    decrypted = "".join([chr(ord(x) - key) for x in message])

    pattern_decrypted = "(?<=@)([a-zA-Z]+)[^@\-!:>]*?:(\d+)[^@\-!:>]*?!([AD]{1})[^@\-!:>]*?!->(\d+)"
    m = re.findall(pattern_decrypted, decrypted)
    planet, population, attack_type, soldier_count = m[0]

    if attack_type == "A":
        data["attacked"].append(planet)
    elif attack_type == "D":
        data["destroyed"].append(planet)

for index, attack in sorted(data.items(), key=lambda x: x[0]):
    if index == "attacked":
        print("Attacked planets: {0}\n-> {1}".format(len(data[index]),"\n->".join(data[index])))
    else:
        print("Destroyed planets: {0}\n-> {1}".format(len(data[index]),"\n->".join(data[index])))

