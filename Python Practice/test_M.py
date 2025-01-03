import car
import bike

car1 = car.Car("Sedan", "Black", 100)
bike1 = bike.Bike("Sports Bike", "White", 80)

car1.accelerate(20)
bike1.brake(10)

car1.display_info()
bike1.display_info()