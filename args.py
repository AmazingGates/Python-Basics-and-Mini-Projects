# *args (The (*) is the most important part. We can have any value attached to it and it would function properly. 
# It is common Python practice to use (args)) - A parameter that will pack all arguments into a tuple.
# Allows our functions to take a varying amount of arguments
def add(*args): # This allowed us to pass more than two parameters to our print()
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3))