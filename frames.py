# Frames - A rectangular container to group and hold widgets

from tkinter import *

def click():
    print("Wet")

def click2():
    print("And")

def click3():
    print("Presents")

def click4():
    print("Slippery")

window = Tk()

frame = Frame(window,bg="orange",bd=5,relief=SUNKEN) # Using the Frame() allows us to add all of our buttons into one container. It do this by
#removing window from our Button() and replace it with frame(the varable for our Frame()). Our Frame() will get
#passed the window. Frame(window) bd= gallows us to create a border. relief= allows us to change the bd= appearence 

frame.pack(side=BOTTOM) # This allows us to put our frame where we want in the window
#frame.place(x=100,y=100) # This place() is another way of fixing our frames coordinates within the window


#button = Button(window,text="W",font=("Consolas",25),width=3)
Button(frame,text="W",font=("Consolas",25),width=3,command=click).pack(side=TOP) # This the same function as above, but without the variable.
                                                            #We do not need to name our function so we'll use this version
Button(frame,text="A",font=("Consolas",25),width=3,command=click2).pack(side=LEFT)
Button(frame,text="P",font=("Consolas",25),width=3,command=click3).pack(side=RIGHT)
Button(frame,text="S",font=("Consolas",25),width=3,command=click4).pack(side=BOTTOM)




#button.pack() # Since we don't have a variable(button) the .pack goes directly onto the function

window.mainloop()