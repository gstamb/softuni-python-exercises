from project.computer_types.computer import Computer

LAPTOP_PROCESSORS = {'AMD Ryzen 9 5950X': 900,
                     'Intel Core i9-11900H': 1050,
                     'Apple M1 Pro': 1200
                     }

LAPTOP_RAM = {2: 100, 4: 200, 8: 300, 16: 400, 32: 500, 64: 600}


def get_processor_price(processor):
    if processor in LAPTOP_PROCESSORS:
        return processor, LAPTOP_PROCESSORS[processor]
    else:
        return False


def get_ram_price(ram):
    if ram in LAPTOP_RAM:
        return ram, LAPTOP_RAM[ram]
    else:
        return False


class Laptop(Computer):
    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        processor_price = get_processor_price(processor)
        ram_price = get_ram_price(ram)

        if processor_price and ram_price:
            self.processor = processor
            self.price += processor_price[1]
            self.ram = ram
            self.price += ram_price[1]
            return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

        else:
            if not processor_price:
                raise ValueError(
                    f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")
            if not ram_price:
                raise ValueError(
                    f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")
