class Car:
    def __init__(self,model,color,speed=0):
        self.model=model
        self.color=color
        self.speed=speed

    def accelerate(self,increment):
        self.speed+=increment
        print(f"your {self.model} {self.color} car is now accelerating with {self.speed} Km/hr")

    def brake(self,decrement):
        self.speed-=decrement
        print(f"your {self.model} {self.color} car is now braking with {self.speed} Km/hr")

    def display_info(self):
        print(f"Car Information:")
        print(f"Color: {self.color}")
        print(f"Speed: {self.speed} km/h")
        print(f"Model: {self.model}")