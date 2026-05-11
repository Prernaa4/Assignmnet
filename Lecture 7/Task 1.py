class Car:
    def __init__(self, v1, v2, v3, v4):
        self.registration_number = v1
        self.maximum_speed = v2
        self.current_speed = v3
        self.travelled_distance = v4


car = Car("ABC-123", 142, 0, 0)

print("Registration Number:", car.registration_number)
print("Maximum Speed:", car.maximum_speed)
print("Current Speed:", car.current_speed)
print("Travelled Distance:", car.travelled_distance)