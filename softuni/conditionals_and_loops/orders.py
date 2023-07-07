orders = int(input())

grand_total = 0
for order in range(orders):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if 0.01 <= capsule_price <= 100.00 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        order_total = capsule_price * days * capsules_per_day
        print(f"The price for the coffee is: ${order_total:.2f}")
        grand_total += order_total

print(f"Total: ${grand_total:.2f}")
