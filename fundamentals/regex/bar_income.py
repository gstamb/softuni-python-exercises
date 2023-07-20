import re

pattern = "%([A-Z]{1}[a-z]+)%[^$|.%]*?<(\w+)>[^$|.%]*?\|[^$|.%]*?(\d+?)\|[^$|.%]*?(\d+?(?:\.\d+?)?)\$"
total = 0
while True:
    string = input()
    if string == "end of shift":
        break

    m = re.findall(pattern, string)
    if m:
        buyer = m[0][0]
        item = m[0][1]
        quantity = float(m[0][2])
        price = float(m[0][3])
        sub_total = quantity*price
        total += sub_total
        print(f"{buyer}: {item} - {sub_total:.2f}")

print(f"Total income: {total:.2f}")