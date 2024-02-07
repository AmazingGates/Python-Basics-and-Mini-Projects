# Buttons - You click it, and then it executes.

from tkinter import *

count = 0

def click(): # This is where we define what our click button does
    global count # This allows us to access the count variable within our function
    count += 1 # This will count and increment by one with each click
    print("For The House Of Gates!!!")
    print(count) # Every time we click our button, our count will increase by 1 and print the result

window = Tk()

photo = PhotoImage(file="Alia 33.png")

button = Button(window, 
                text="Para La Casa",
                command=click,
                font=("Italic", 30),
                fg="red",
                bg="black",
                activeforeground="red",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="left") # This is how we create a button. The Button() takes the an argument of the
                        #place where it will run, (Button(window))
# window - where our button will be displayed
# text - Allows us to name our button
# Command - creates a function call back. using the click without the () lets the program know it is a callback. 
#This means that whenever clicked, it will callback whatever function is written in def click():
# font - allows us to change the font of the button name. You can also change the font size through font
# fg - allows us to change the color of the button text
# bg - changes the color of the background 
# activeforeground - allows us to change the color of the activeforeground, to help stop button text
#color flash when clicked
# activebackground - allows us to change the color of the activebackground, to help stop background
#color flash when clicked
# state - is usually active, but once switched to disabled, it will block access to the click()
# photo - allows us to add an image to our button, but using photo alone, it will replace our text
#so we have to use the compound method
# compound - allows us to add both an image and text to our button

button.pack() # This is how we display the button in our GUI window

window.mainloop()