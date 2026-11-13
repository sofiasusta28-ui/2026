class WaterPump:

    def __init__(self, power=0, brand="Невідомо", volume=0):
        self.__brand = brand
        self.__volume = volume
        self.__power = power
        self.pump_type = "Центробіжний"
        self.warranty = 24


    def __del__(self):
        print(f"Об'єкт '{self.__brand}' видалено з пам'яті.")

    def get_power(self):
        return self.__power

    def get_brand(self):
        return self.__brand

    def get_volume(self):
        return self.__volume

    def __str__(self):
        return f"Насос '{self.__brand}' ({self.__power} Вт, {self.__volume} л/год)"

    def __repr__(self):
        return f"WaterPump({self.__power}, '{self.__brand}', {self.__volume})"


def main():
    print("___ Створення об'єктів ___")

    p1 = WaterPump()
    p2 = WaterPump(750, "Pedrollo", 3600)
    p3 = WaterPump(1100, "Aquatica", 5000)
    pumps = [p1, p2, p3]
    print("\n___ Виведення полів об'єктів ___")
    for p in pumps:
        print("----------------------------")
        print(f"Марка: {p.get_brand()}")
        print(f"Потужність: {p.get_power()} Вт")
        print(f"Продуктивність: {p.get_volume()} л/год")

        print(f"Тип: {p.pump_type}")
        print(f"Гарантія: {p.warranty} місяців")

        print(f"Метод __str__: {p}")
        print(f"Метод __repr__: {repr(p)}")

    print("\n___ Кінець програми ___")

main()