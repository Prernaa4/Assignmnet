import random

print("Guess number between 1 and 10")

number = random.randint(1, 10)

guess = int(input("Enter your guess: "))

while guess != number:
    if guess > number:
        print("Too high")
    else:
        print("Too low")

    guess = int(input("Guess again: "))

print("Correct!")