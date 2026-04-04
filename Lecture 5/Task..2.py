messages = ("New name", "Existing name")

names = set()

name_status = {}

while True:
    name = input("Enter name (or press Enter to stop): ")

    if name == "":
        break

    if name in names:
        print(messages[1])
    else:
        print(messages[0])
        names.add(name)
        name_status[name] = "Added"

print("\nUnique names:")
for n in names:
    print(n)