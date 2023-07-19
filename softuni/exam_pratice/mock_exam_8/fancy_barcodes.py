import re

for _ in range(int(input())):
    string = input()

    pattern = "@#{1,}([A-Z][a-zA-Z0-9]{4,}[A-Z])@#{1,}"

    match = re.findall(pattern, string)
    if match:
        product_group = [x for x in match[0] if x.isdigit()]
        if not product_group:
            print("Product group: 00")
        else:
            print(f"Product group: {''.join(product_group)}")
    else:
        print("Invalid barcode")
