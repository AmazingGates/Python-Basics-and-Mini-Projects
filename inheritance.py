# Inheritance - With an inheritance, we can pass attributes and meyhods of parent functions to their children
class Animal:

    alive = True

    def eat(self):
        print("This animal is eating.")

    def sleep(self):
        print("This animal is sleeping.")

class Rabbit(Animal): # By inserting the Animal class into the Rabbit class, we are indicating that Rabbit is a Child of
    def run(self):    # #Animal. Animal is the PArent class. Because of this dynamic, Rabbit we inherit everything
        print("The Rabbit is running.")    #the Animal class has          
                      

class Fish(Animal): # This Fish will inherit all the attributes and methods of its Parent, Animal
    def swim(self):
        print("The Fish is swift when it swims.")


class Hawk(Animal): # This Hawk will inherit all the attributes and methods of its Parent, Animal
    def flight(self):
        print("The Hawk in flight is poetry in motion.")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()


print(rabbit.alive)
fish.eat()
hawk.sleep()
rabbit.run()
fish.swim()
hawk.flight()