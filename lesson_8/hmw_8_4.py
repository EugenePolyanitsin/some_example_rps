
class OfficeEquipmentWarehouse:
    storage: dict = {}

    def __init__(self):

        pass

    def add_equipment(self, equipment, count):

        equipment_type = equipment.__class__.__name__
        try:
            self.storage[equipment_type][equipment.name] += count
        except KeyError:
            if equipment_type not in self.storage:
                self.storage[equipment_type] = {}
                self.storage[equipment_type][equipment.name] = count
            elif equipment.name not in self.storage[equipment_type]:
                self.storage[equipment_type][equipment.name] = count


    def __str__(self):
        output = ''
        for k, equipment in self.storage.items():
            output += f'{k}:\n'
            print(equipment)
            for e, count in equipment.items():
                output += f'\t{e} {count}\n'

        return output



class OfficeEquipment:
    name: str = None
    weight: float = float()
    __price: float = None

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        try:
            self.__price = float(price)
        except ValueError:
            print(f"price {price} is not a number")
            self.__price = None

    def __str__(self):
        return f'{self.name} {self.price} {self.weight}'


class Printer(OfficeEquipment):
    print_formats = ["A2", "A3", "A4", "A5"]
    print_format: str = None
    colored: bool = False

    def __init__(self, name, weight, price, print_format, colored):
        super(Printer, self).__init__(name, weight, price)
        self.print_format = print_format
        self.colored = colored

    def __str__(self):
        return '{name} {print_format} {colored} {price}руб {weight}кг' \
            .format(
            name=self.name,
            print_format=self.print_format,
            colored="colored" if self.colored else "monochrome",
            price=self.price,
            weight=self.weight
        )


class Scaner(OfficeEquipment):
    scan_formats = ["A2", "A3", "A4", "A5"]
    scan_format: str = None

    def __init__(self, name, weight, price, scan_format):
        super(Scaner, self).__init__(name, weight, price)
        self.scan_format = scan_format




    def __str__(self):
        return '{name} print {print_format} scan {scan_format} {colored} {price}руб {weight}кг' \
            .format(
            name=self.name,
            print_format=self.print_format,
            scan_format=self.scan_format,
            colored="colored" if self.colored else "monochrome",
            price=self.price,
            weight=self.weight
        )


if __name__ == '__main__':
    storage = OfficeEquipmentWarehouse()
    oo = OfficeEquipment("01", 1, "4000")
    p1 = Printer(
        name="P1",
        weight=3,
        price="6000",
        print_format="A4",
        colored=True
    )
    s1 = Scaner(
        "S1",
        weight=1,
        price="3000",
        scan_format="A3")

    s2 = Scaner(
        "S2",
        weight=1,
        price="5500",
        scan_format="A5")


    print(oo)
    print(p1)
    storage.add_equipment(p1, 3)
    storage.add_equipment(p1, 2)
    storage.add_equipment(s1, 6)
    storage.add_equipment(s2, 2)
    print(storage)
