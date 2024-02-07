# Higher Order Functions - A Function that either: 1. accepts a function as an argument or 2. returns a function
# In Python, functions are also treated as objects

# This is part 1 of the example
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func): # This is an example of a higher order function. Notice how the hello() accepts a function(func) as 
    text = func("Hello") #an argument
    print(text)


hello(loud)
hello(quiet)


# This is aprt 2 of the example

def divisor(x): # Divisor is considered a higher order function because it is returning a function, dividend()
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))