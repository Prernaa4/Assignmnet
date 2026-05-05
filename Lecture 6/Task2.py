def convert(g):
    return g * 3.785

g = float(input("Enter gallons: "))

while g >= 0:
    print("Litres:", convert(g))
    g = float(input("Enter gallons: "))