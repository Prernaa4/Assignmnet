smallest = None
largest = None

num = input("Enter number: ")

while num != "":
    num = float(num)

    if smallest is None or num < smallest:
        smallest = num

    if largest is None or num > largest:
        largest = num

    num = input("Enter number: ")

if smallest is not None:
    print("Smallest:", smallest)
    print("Largest:", largest)
else:
    print("No numbers entered")