class Car:
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def display_details(self):
        print(f"Car: {self.year} {self.make} {self.model}, Speed: {self.speed} km/h")

    def check_speed(self):
        if self.speed > 100:
            return "Speeding!"
        else:
            return "Safe speed"

car1 = Car("Nissan", "Versa", 2015, 120)
car1.display_details()
print(car1.check_speed())  