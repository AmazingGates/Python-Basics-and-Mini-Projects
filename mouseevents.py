# Mouse Events - In this section we will be going over the process of creating mouse events
# The mouse events is similar to the keyboard events, but instead of keys, the mouses position triggers our function
#and displays the mouses current location in our window

from tkinter import *

def doSomething(event):
    print("Mouse Coordinates: " + str(event.x)+","+str(event.y)) # str(event.x) and str(event.y) allows us to get the 
    #the coordinates of the "x" and "y" loction when the event occurs. the str is used because the coordinates are
    #are integers and need to be converted to strings to display properly


window = Tk()


window.bind("<Button-1>",doSomething) # <Button-1> represents a left click on our mouse
#window.bind("<Button-2>",doSomething) # <Button-2> represents a scroll wheel use on our mouse 
                                       #(takes action once we push the wheel)
#window.bind("<Button-3>",doSomething) # <Button-3> represents a right click on our mouse
#window.bind("<ButtonRelease>",doSomething) # <ButtonRelease> event will be activated once we release our key
#window.bind("<Enter>",doSomething) # <Enter> activates event once we enter the window
#window.bind("<Leave>",doSomething) # <Leave> activates event once we leave the window
#window.bind("<Motion>",doSomething) # <Motion>  activates event where ever our mouse is in the window and will 
                            #continue to update the mouses "x" and "y" coordinates with any mouse motion within
                            #our window


window.mainloop()