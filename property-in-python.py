class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature


    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


    """ Объект считать и записать новое значение данных атрибутам """
    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature


    """ Сэттер проверить значения. Сперва проверяет значение с init по умолчанию для температуры """
    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value




human = Celsius()
human.temperature = 30

print(human.__dict__)  # Проверить словарь данных класса
print(human.to_fahrenheit())



"""
class House:

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return f'${self._price}'
    
    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price")

    @price.deleter
    def price(self):
        del self._price


house = House(-50000.0)
# del house.price
print(house.price)

"""