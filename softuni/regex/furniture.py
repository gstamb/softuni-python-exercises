import re

items = []
tot_spend = 0
while True:

    purchase = input()
    if purchase == "Purchase":
        break

    pattern = r">>([a-zA-Z_]+)<<([0-9]+(?:\.[0-9]+)?)!([0-9]+)"
    matches = re.findall(pattern, purchase)
    item_to_buy = ""
    if matches:
        for m in matches:
            item = m[0]
            price = m[1]
            quantity = m[2]
            items.append(item)
            tot_spend += int(quantity) * float(price)

print("Bought furniture:")
[print(x) for x in items]
print(f"Total money spend: {tot_spend:.2f}")
