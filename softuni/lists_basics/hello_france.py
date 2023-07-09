CLOTHES = 50
SHOES = 35
ACCESSORIES = 20.50

offered_items = [x for x in input().split("|")]
budget = float(input())
spent = 0
sold = 0
for offer in offered_items:
    item, price = offer.split("->")
    price = float(price)

    if item == "Clothes":
        if price <= CLOTHES:
            if budget >= price:
                budget -= price
                spent += price

                new_price = price * 1.4
                sold += new_price
                print(f"{new_price:.2f}", end=" ")
    elif item == "Shoes":
        if price <= SHOES:
            if budget >= price:
                budget -= price
                spent += price

                new_price = price * 1.4
                sold += new_price
                print(f"{new_price:.2f}", end=" ")
    elif item == "Accessories":
        if price <= ACCESSORIES:
            if budget >= price:
                budget -= price
                spent += price
                new_price = price * 1.4
                sold += new_price
                print(f"{new_price:.2f}", end=" ")

print()
print(f"Profit: {sold-spent:.2f}")
if sold+budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")


