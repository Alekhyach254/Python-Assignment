phonebook = {
    "Michael": "123-456-7890",
    "John": "987-654-3210",
    "Joseph": "555-666-7777"
}

def lookup_phonebook():
    while True:
        name = input("Enter a name to look up (or type 'exit' to quit): ").strip()
        if name.lower() == 'exit':
            print("Exiting phonebook lookup.")
            break
        elif name in phonebook:
            print(f"{name}'s phone number is: {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook.")

# Run the phonebook lookup
lookup_phonebook()