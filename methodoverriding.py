# Method Overriding - Is the ability of an oop langauge to allow a sub class or child class to provide a specific
#implementation of a method that is already provided by one of its parents

class Animal:

    def eat(self): # This is the method that the parent would normally pass on to a child class.
        print("This Animal is eating.")

class Rabbit(Animal):

    def eat(self): # This is an example of method overriding. Bascically, an object will use a method more closely 
        print("This Rabbit is eating a carrot!") #associated with itself before it uses an outside method

rabbit = Rabbit()
rabbit.eat()