# Abstract Classes - A class which contains one or more abstract methods
# Prevents a user from creating an object of that class
# Compels a user to override abstract methods
# Abstract Method - A method that has a declaration but does not have an implementation
# abc stands for "abstract based class"

from abc import ABC, abstractmethod

class Vehical(ABC): # This is an example turning a class into an abtract class. Turning class into an abstract class
                    #helps us prevent users from creating an object of this class
    @abstractmethod # This decorator goes above any method inside your (ABC) class.
    def go(self): # All children must override this method and initiate their own.
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehical):

    def go(self):
        print("You are driving the car.")

    def stop(self):
        print("Slow down and pull over.")


class Motorcycle(Vehical):

    def go(self):
        print("You are riding your motorcycle.")

    def stop(self):
        print("You need to park your bike")

print("--------------------------------------------------")
print("--------------------------------------------------")

car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()


print("--------------------------------------------------")
print("--------------------------------------------------")


car.stop()
motorcycle.stop()

print("--------------------------------------------------")
print("--------------------------------------------------")