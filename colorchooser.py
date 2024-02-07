# Color Chooser - In this section we will be creating a color chooser

from tkinter import *
from tkinter import colorchooser # This is a submodule

def click():
    color = colorchooser.askcolor() # Function we use to select a color and get its rgba() number / hexidecimal number
    print(color) # This is how we print the color we selected to our terminal
    colorHex = color[1] # This is how target the element at position 1 (Second Element (#ff0000))
    print(colorHex) # This is how we print the indexed color[1]
    window.config(bg=colorHex) # This is how we apply our color selection to our background
    #print("The Beginning Of 2024 - Brian Javelle and Alia Marie Will Start \
#An Ever Lasting Romantic Relationship That Leads To A Long Loving Marriage")

window = Tk()

window.geometry("420x420") # This is how we set the width and height of our window
button = Button(text="Click Me",
                command=click)

#button.config(text="Click Me")
#button.config(command=click)

button.pack()

window.mainloop()