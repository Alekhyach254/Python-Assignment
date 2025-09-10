class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        return f"Vehicle Name: {self.name}, Speed: {self.max_speed} km/h, Mileage: {self.mileage} km/l"


class Bike(Vehicle):
    def __init__(self, name, max_speed, mileage, type_of_bike):
        super().__init__(name, max_speed, mileage)
        self.type_of_bike = type_of_bike

    def display_info(self):
        return f"Bike - {super().display_info()}, Type: {self.type_of_bike}"


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity):
        super().__init__(name, max_speed, mileage)
        self.capacity = capacity

    def display_info(self):
        return f"Bus - {super().display_info()}, Seating Capacity: {self.capacity}"


if __name__ == "__main__":
    bike = Bike("Yamaha R15", 150, 40, "Sports")
    bus = Bus("Volvo", 120, 6, 50)

    print(bike.display_info())
    print(bus.display_info())