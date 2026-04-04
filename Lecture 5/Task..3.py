airports = {}

while True:
    print("\n1. Enter new airport: ")
    print("2. Fetch airport")
    print("3. Quit")

    choice = input("Choose option: ")

    if choice == "1":
        code = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[code] = name
        print("Airport saved!")

    elif choice == "2":
        code = input("Enter ICAO code: ")
        if code in airports:
            print(airports[code])
        else:
            print("Airport not found")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")