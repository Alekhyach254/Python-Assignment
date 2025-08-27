class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display_details(self):
        print(f"Car Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")


# Creating an object of Car class
my_car = Car("Toyota", "Camry", 2022, "White")

# Printing the details of the object
my_car.display_details()