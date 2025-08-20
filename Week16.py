class NegativeAgeError(Exception):
    def __init__(self, age, message="Age cannot be negative"):
        self.age = age
        self.message = message
        super().__init__(f"{message}. You entered: {age}")


def check_age(age):
    if age < 0:
        raise NegativeAgeError(age)
    else:
        print(f"Valid age entered: {age}")


try:
    age = int(input("Enter your age: "))
    check_age(age)
except NegativeAgeError as e:
    print("Error:", e)