# Multi_Level Inheritance - When a derived (child) class inherits from another derived (child) class
class Organism: # This is the parent class
    
    alive = True

class Animal(Organism): # This is a child class, which will inherit from its parent(Organism)
    
    def eat(self):
        print("This Animal is eating.")

class Dog(Animal): # This is a child class which will inherit its attributes and methods from another child class
    
    def bark(self): #(Animal). This is an example of multi_level inheritance
        print("The Dog is barking loudly!")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()