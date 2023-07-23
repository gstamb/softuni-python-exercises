from collections import deque
from collections import Counter


def craft_presents(materials, magic_quantity, presents, crafted_products):
    while magic_quantity and materials:

        material = materials.pop()
        magic = magic_quantity.popleft()
        product = magic * material

        if product in presents:
            crafted_products.append(presents[product])
            continue

        if product < 0:
            material += magic
            materials.append(material)
        elif product > 0:
            material += 15
            materials.append(material)
        elif product == 0:
            if material != 0:
                materials.append(material)
            if magic != 0:
                magic_quantity.appendleft(magic)
 

def print_result(crafted_products, materials, magic_quantity):
    if ("Doll" in crafted_products and "Wooden train" in crafted_products) \
            or \
            ("Teddy bear" in crafted_products and "Bicycle" in crafted_products):
        print("The presents are crafted! Merry Christmas!")
    else:
        print("No presents this Christmas!")

    if materials:
        print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
    if magic_quantity:
        print(f"Magic left: {', '.join([str(x) for x in magic_quantity])}")
    counter = Counter(crafted_products)
    for count, val in sorted(counter.items()):
        print(f"{count}: {val}")


def main():
    materials = deque(map(int, input().split()))
    magic_quantity = deque(map(int, input().split()))

    presents = {
        150: "Doll",
        250: "Wooden train",
        300: "Teddy bear",
        400: "Bicycle"
    }
    crafted_products = []

    craft_presents(materials, magic_quantity, presents, crafted_products)

    print_result(crafted_products, materials, magic_quantity)


if __name__ == "__main__":
    main()
