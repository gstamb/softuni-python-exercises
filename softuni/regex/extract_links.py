import re

links = []
while True:
    string = input()
    if string == "":
        break

    pattern = "(www.([0-9a-zA-Z]+(?:[0-9a-zA-Z-]+)?)(([.][a-zA-Z]+)+))"
    matches = re.findall(pattern, string)
    item_to_buy = ""
    if matches:
        for m in matches:
            link = m[0]
            links.append(link)


for link in links:
    print(link)


