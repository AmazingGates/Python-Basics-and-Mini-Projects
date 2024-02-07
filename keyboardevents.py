# Keyboard Events - In this section we will be going over the process of creating Keyboard Events
# We can bind a key event and function to a widget or window so that when we push a certain key or do something
#we can trigger a function to be called that will perform some sort of task for us.

from tkinter import *

#def doSomething(event): # Our function that is bound needs an (event), very important
    #print("Brian Javelle and Alia Marie Gates...")

#def doSomething(event):
    #print("Long Live Gates")

#def doSomething(event):
    #print("Para La Casa..")

def doSomething(event):
    print("You pressed: " + event.keysym) # Using the event.keysym in our print statement will allow us to display
                                       #whick key was pressed
    label.config(text=event.keysym)


window = Tk()

#window.bind("<Return>",doSomething) # The bind() is how we bind our key events and functions. The bind() takes an event and a function
              #(bind(event,function)) Also this is how we desinate which key we want to Bind "<B>".
              # Using the <Return> input allows us to perform a function  once our enter key is pushed

#window.bind("<q>",doSomething) # Using the <q> input, allows us to perform a function when the "q" key
window.bind("<Key>",doSomething) # Using the <Key> input with a capital K allows us to activte almost all the letters


label = Label(window,font=("times roman",100))
label.pack()


window.mainloop()