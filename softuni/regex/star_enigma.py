import re

data = {"attacked": [], "destroyed": []}
for messages in range(int(input())):
    message = input()

    pattern = "(?i)(?:[star])"
    m = re.findall(pattern, message)

    key = len(m)
    decrypted = "".join([chr(ord(x) - key) for x in message])

    pattern_decrypted = r"(?<=@)([a-zA-Z]+)[^@\-!:>]*?:(\d+)[^@\-!:>]*?!([AD])![^@\-!:>]*?->(\d+)"
    m = re.findall(pattern_decrypted, decrypted)
    if m:
        planet, population, attack_type, soldier_count = m[0]

        if attack_type == "A":
            data["attacked"].append(planet)
        elif attack_type == "D":
            data["destroyed"].append(planet)

for index, attack in data.items():
    if index == "attacked":
        if len(data[index]) > 0:
            print("Attacked planets: {0}\n-> {1}".format(len(data[index]), "\n-> ".join(sorted(data[index]))))
        else:
            print("Attacked planets: {0}".format(len(data[index])))

    else:
        if len(data[index]) > 0:
            print("Destroyed planets: {0}\n-> {1}".format(len(data[index]), "\n-> ".join(sorted(data[index]))))
        else:
            print("Destroyed planets: {0}".format(len(data[index])))
