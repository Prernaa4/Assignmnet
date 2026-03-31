length = float(input("Enter the length of zander (cm): "))

if length >= 42:
    print("You can keep the fish.")

else:
    short = 42 - length
    print("Release the fish back into the lake.")
    print("It is", short, "cm below the size limit.")