# Python Object Oriented Programming - An object is an instance of a class
# To create an object we have to create a Class
# A Class can function as a blueprint that will describe what attributes and methods that our distinct object has
# When using classes, it is best practice to set it up in separate module and then import it over to your actual code
#in case the classes become too big of a file.
# This file isn't that big but we set it up as a separate module just to go over the process
# Objects can have a combination of attributes and methods
# We will also be using the def__init__self(), which is know as the constructor method
# (self) refers to the object that is using the method
# This module should be imported to our oop.py file
class Car: # It is common practice to capitalize class names

    wheels = 4 # This is an example of a class variable. A class variable is declared inside the class, but outside 
               #the constructor

    def __init__(self,make,model,year,color):  # Constructor method that will create objects for us
        self.make = make # These are attributes and instance variables. Instance variables are created inside the
        self.model = model #constructor
        self.year = year 
        self.color = color 

    def drive(self):  # These are methods
        print("This car is driving")
   
    def stop(self):
        print("This car is stopped")