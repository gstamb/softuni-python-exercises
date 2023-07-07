budget = float(input())
price_flour = float(input())
price_milk = ( price_flour * 1.25 ) / 4
price_eggs = price_flour * 0.75
price_per_loaf = price_eggs + price_flour + price_milk

colored_eggs = 0
bread_count = 0
while budget > price_per_loaf:
    budget -= price_per_loaf
    bread_count += 1
    colored_eggs += 3

    if bread_count % 3 == 0:
        colored_eggs -= bread_count -2


print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
