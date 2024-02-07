# **kwargs (The same rules apply with the importance the (**) vs the importance of (kwargs))
# A parameterthat will pack all arguments into a dictionary dict/{}.
# This allows our functions to accept a varying amount of keyword arguments.
import time

def hello(**kwargs):
    print("Hello " + kwargs["first"] + " " + kwargs["last"])
    
hello(first= "Brian", middle= "Javelle", last= "Gates")

# In the example below we will tweak the code above so that we may return a users full name(title,first,middle,last)
def hello(**kwargs):
    print("Hello", end=" ")
    time.sleep(1)
    for key,value in kwargs.items():
        print(value, end=" ")

hello(title= "Mr.", first= "Brian", middle= "Javelle", last= "Gates")