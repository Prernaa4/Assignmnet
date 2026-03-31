gender = input("Enter gender (male/female): ")
hb = float(input("Enter hemoglobin level (g/L): "))

if gender == "female":
    if hb < 117:
        print("Hemoglobin level is low.")
    elif hb <= 155:
        print("Hemoglobin level is normal.")
    else:
        print("Hemoglobin level is high.")

elif gender == "male":
    if hb < 134:
        print("Hemoglobin level is low.")
    elif hb <= 167:
        print("Hemoglobin level is normal.")
    else:
        print("Hemoglobin level is high.")

else:
    print("Invalid gender")