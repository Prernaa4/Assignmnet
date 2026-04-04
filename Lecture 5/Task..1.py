seasons = ("Winter", "Spring", "Summer", "Autumn")

month_to_season = {
    12: "Winter", 1: "Winter", 2: "Winter",
    3: "Spring", 4: "Spring", 5: "Spring",
    6: "Summer", 7: "Summer", 8: "Summer",
    9: "Autumn", 10: "Autumn", 11: "Autumn"
}

valid_months = {1,2,3,4,5,6,7,8,9,10,11,12}

month = int(input("Enter month (1-12): "))

if month in valid_months:
    print(month_to_season[month])
else:
    print("Invalid month")