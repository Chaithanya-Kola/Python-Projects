class Bike:
    def __init__(self, model,color,speed=0):
        self.color = color
        self.speed = speed
        self.model = model

    def accelerate(self, increment):
        self.speed += increment
        print(f"{self.model} is accelerating. New speed: {self.speed} km/h")

    def brake(self, decrement):
        self.speed -= decrement
        print(f"{self.model} is braking. New speed: {self.speed} km/h")

    def display_info(self):
        print(f"Bike Information:")
        print(f"Color: {self.color}")
        print(f"Speed: {self.speed} km/h")
        print(f"Model: {self.model}")