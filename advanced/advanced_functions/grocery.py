def grocery_store(**kwargs):
    """
    Receives a list of items and quantity and returns a sorted receipt.

    :param kwargs: key value pairs of food products and quantity
    :return: a receipt of product and quantity sorted in:
    descending order of quantity, the length of product name
    and ascending order of product name
    """
    build_receipt = ""
    for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
        build_receipt += f"{key}: {value}\n"

    return build_receipt


def main():
    print(grocery_store(
        pasta=2,
        bread=2,
        eggs=20,
        carrot=1,
    ))


if __name__ == "__main__":
    main()
