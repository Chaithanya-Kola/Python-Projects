class Cars:
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

car1 = Cars("Sedan","Red",100)
car2 = Cars("SUV","Black",200)
car3 = Cars("HatchBack","Maroon",150)
car4 = Cars("Sportscar","White",500)

while True:
    print("Select a feature:")
    print("1. Accelerate")
    print("2. Brake")
    print("3. Display Car Information")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        car_choice = int(input("Select a car (1, 2, or 3): "))
        increment = int(input("Enter acceleration increment: "))
        if car_choice == 1:
            car1.accelerate(increment)
        elif car_choice == 2:
            car2.accelerate(increment)
        elif car_choice == 3:
            car3.accelerate(increment)
        elif car_choice == 4:
            car4.accelerate(increment)
        else:
            print("Invalid car choice.")

    elif choice == 2:
        car_choice = int(input("Select a car (1, 2, or 3): "))
        decrement = int(input("Enter braking decrement: "))
        if car_choice == 1:
            car1.brake(decrement)
        elif car_choice == 2:
            car2.brake(decrement)
        elif car_choice == 3:
            car3.brake(decrement)
        elif car_choice == 4:
            car4.brake(decrement)
        else:
            print("Invalid car choice.")

    elif choice == 3:
        car_choice = int(input("Select a car (1, 2, or 3): "))
        if car_choice == 1:
            car1.display_info()
        elif car_choice == 2:
            car2.display_info()
        elif car_choice == 3:
            car3.display_info()
        elif car_choice == 4:
            car4.display_info()
        else:
            print("Invalid car choice.")

    elif choice == 4:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
