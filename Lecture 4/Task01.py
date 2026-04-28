import random

num = int(input("How many dice to roll: "))
total = 0

for i in range(num):
    total += random.randint(1, 6)

print("Sum  of dice:", total)