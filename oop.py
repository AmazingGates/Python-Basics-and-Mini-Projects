# This is our first  and second created objects
from car import Car

car_1 = Car("Chevy", "Corvette", 2024, "Blue") # This is our first object
car_2 = Car("Ford", "Mustang", 2024, "Red")  # This is our second object

print("------------------------------------------------------------------")

print(car_1.make) # These are our first objects attributes
print(car_1.model)
print(car_1.year)
print(car_1.color)

print("------------------------------------------------------------------")

#car_1.drive()
car_1.stop()
print("This Car has " + str(car_1.wheels) + " wheels")

print("------------------------------------------------------------------")

print("*")
print("*")
print("And")
print("*")
print("*")

print("------------------------------------------------------------------")

print(car_2.make) # These are our second objects attribbutes
print(car_2.model)
print(car_2.year)
print(car_2.color)

print("------------------------------------------------------------------")

car_2.drive()
#car_2.stop()
print("This Car has " + str(car_2.wheels) + " wheels")

print("------------------------------------------------------------------")