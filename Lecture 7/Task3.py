class Car:

    def __init__(self, max_speed):
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


car = Car(180)

car.current_speed = 60
car.travelled_distance = 2000

car.drive(1.5)

print("Travelled Distance:", car.travelled_distance, "km")