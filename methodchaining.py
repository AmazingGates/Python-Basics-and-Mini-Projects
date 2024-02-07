# Method Chaining - Used to call mutiplemethods sequentially. Each call performs an action on the same object 
#and returns self

class Car:

    def turn_on(self):
        print("You Started the engine.")
        return self # We need to add return self to every method we use in our method chain

    def driving(self):
        print("You are driving the car.")
        return self # We need to add return self to every method we use in our method chain

    def brake(self):
        print("Slow Down, and pull over.")
        return self # We need to add return self to every method we use in our method chain

    def turn_off(self):
        print("Turn of the engine.")
        return self # We need to add return self to every method we use in our method chain

car = Car()
car.turn_on().driving().brake().turn_off() # This is an example of method chaining. We dont have to use all of the
                                           #methods, and the ones we do use will be call sequentially in the order
                                           #we set them.
