from project.computer_types.computer import Computer

DESKTOP_PROCESSORS = {'AMD Ryzen 7 5700G': 500,
                      'Intel Core i5-12600K': 600,
                      'Apple M1 Max': 1800
                      }

DESKTOP_RAM = {2: 100, 4: 200, 8: 300, 16: 400, 32: 500, 64: 600, 128: 700}


def get_processor_price(processor):
    if processor in DESKTOP_PROCESSORS:
        return processor, DESKTOP_PROCESSORS[processor]
    else:
        return False


def get_ram_price(ram):
    if ram in DESKTOP_RAM:
        return ram, DESKTOP_RAM[ram]
    else:
        return False


class DesktopComputer(Computer):
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
                    f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")
            if not ram_price:
                raise ValueError(
                    f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")


