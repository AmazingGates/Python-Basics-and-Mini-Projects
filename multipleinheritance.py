# Multiple Inheritance - When a child class is derived from more than one parent class
class Prey:

    def flee(self):
        print("This Animal needs to escape!")


class Predator:

    def hunt(self):
        print("While this animal needs to catch it.")


class Rabbit(Prey):
    pass

class Fox(Predator):
    pass

class Fish(Predator, Prey): # This is an example of multiple inheritance. The class Fish has inherited attributes and 
    pass                    #methods from both parent classes, Predator and Prey

rabbit = Rabbit()
fox = Fox()
fish = Fish()

print("------------------------------------------------------------------")

rabbit.flee()
fox.hunt()

print("------------------------------------------------------------------")

fish.flee()
fox.hunt()

print("------------------------------------------------------------------")

