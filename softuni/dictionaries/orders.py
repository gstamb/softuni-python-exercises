order = {}

while True:
    entry = input()
    if entry == "buy":
        break

    product, price, quantity = entry.split()

    if product in order:
        order[product][0] = float(price)
        order[product][1] += int(quantity)
    else:
        order[product] = []
        order[product].append(float(price))
        order[product].append(int(quantity))

for product, details in order.items():
    quantity, price = details
    print(f"{product} -> {quantity * price:.2f}")
