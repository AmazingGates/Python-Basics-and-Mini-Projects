# Objects As Arguments - This is an example on how to pass objects as arguments
class Car:

    color = None

class Motorcycle:

    color = None

def change_color(car, color):

    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()
bike_2 = Motorcycle()
bike_3 = Motorcycle()

change_color(car_1, "Red") # This is an example of passing an object as an argument (car_1) = object/argument.
change_color(car_2, "White") #(change_color) = method
change_color(car_3, "Blue")

change_color(bike_1, "Red")
change_color(bike_2, "Green")
change_color(bike_3, "Black")

print("--------------------------------------------------")
print("--------------------------------------------------")

print(car_1.color)
print(car_2.color)
print(car_3.color)

print("--------------------------------------------------")
print("--------------------------------------------------")

print(bike_1.color)
print(bike_2.color)
print(bike_3.color)

print("--------------------------------------------------")
print("--------------------------------------------------")