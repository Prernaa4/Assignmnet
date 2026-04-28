numbers = []

num = input("Enter a number (or press Enter to quit): ")

while num != "":
    numbers.append(int(num))
    num = input("Enter a number (or press Enter to quit): ")

numbers.sort(reverse=True)

print("Top 5 numbers:", numbers[:5])