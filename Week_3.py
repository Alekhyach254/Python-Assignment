
age = int(input("Please enter your age: "))
if age < 18:
    print("You are minor.")
elif 18 <= age < 65:
    print("You are adult.")
else:
    print("You are senior.")
