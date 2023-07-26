def shop_from_grocery_list(*args):
    """
    Function checks if a shopping list can be fulfilled within a specified budget and desired list of items.
    :param args: Budget, Grocery List and Available items
    :return: Success message string upon successful shopping and remaining budget
             or a list of the products that could not have not been bough.
    """
    budget = args[0]
    needed_items = args[1]
    available_items = args[2:]

    items_bought = {"items": [], "total_price": 0}

    for item in available_items:
        product, price = item
        if product not in items_bought["items"] and product in needed_items:
            if items_bought["total_price"] + price > budget:
                break
            else:
                items_bought["items"].append(product)
                items_bought["total_price"] += price

    difference = set(needed_items).difference(items_bought["items"])

    if difference:
        return f"You did not buy all the products. Missing products: {', '.join(difference)}."
    else:
        return f"Shopping is successful. Remaining budget: {budget - items_bought['total_price']:.2f}."


def main():
    print(shop_from_grocery_list(
        100,
        ["tomato", "cola", "chips", "meat", "chocolate"],
        ("cola", 15.8),
        ("chocolate", 30),
        ("tomato", 15.85),
        ("chips", 50),
        ("meat", 22.99),
    ))


if __name__ == "__main__":
    main()
