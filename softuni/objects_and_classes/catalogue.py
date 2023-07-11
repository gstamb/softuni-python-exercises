class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        product_list = [x for x in self.products if x.startswith(first_letter)]
        return product_list

    def __repr__(self):
        result = "Items in the {0} catalogue:\n" \
                 "{1}".format(self.name, '\n'.join(sorted(self.products)))
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
catalogue.add_product("Aarpet")
catalogue.add_product("Arpet")
catalogue.add_product("Azpet")
print(catalogue.get_by_letter("C"))
print(catalogue.get_by_letter("A"))
print(catalogue)
