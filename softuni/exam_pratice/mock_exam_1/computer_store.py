total_price = 0
tax_rate = 0.2
discount = 0.1
while True:

    item = input()

    if item == "special" or item == "regular":
        break

    price = float(item)
    if price < 0:
        print("Invalid price!")
        continue


    total_price += price
if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    taxes = total_price * tax_rate
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    payable = total_price + taxes
    if item == "special":
        print(f"Total price: {payable*(1-discount):.2f}$")
    elif item == "regular":
        print(f"Total price: {payable:.2f}$")

