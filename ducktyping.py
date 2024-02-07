# Duck typing - Concept where the class of an oject is less important than the methods/attributes
# Class type is not checked if minimum methods/attributes are present
# "If it waks like a duck, and it quacks like a duck, then it must be a duck."

class Duck:

    def walk(self):
        print("The ducks waddle when they walk.")

    def talk(self):
        print("The ducks quack to communicate.")

class Chicken:

    def walk(self):
        print("Chickens walk more like dinosaurs.")

    def talk(self):
        print("The chicken clucks and the rooster cock a doddle dos!")


class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("The Man is duck hunting!")

duck = Duck()
chicken = Chicken()
person = Person()

print("-------------------------------------------------------------")
print("-------------------------------------------------------------")


person.catch(duck) # Using this method will run all the attributes of both the duck and the person because (duck) was
                   #was passed as an argument to the .catch(). The passed argument (duck) will have its attributes
                   #run first, then the person.