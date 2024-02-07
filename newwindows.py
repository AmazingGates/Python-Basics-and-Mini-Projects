# New Windows - In this section we will be going over a few different ways to create new windows in Python

from tkinter import *

def create_window(): # This function allows us to create a new window while our original window is open
    new_window = Tk() # Toplevel() = new window "on top" of other windows, linked to a "bottom" window

    #old_window.destroy() # This will close our old window once our new window is created
window = Tk()
#old_window = Tk() # This has to be used if we use the destroy()

Button(window,text="Create New Window",command=create_window).pack()
#Button(old_window,text="Create New Window",command=create_window).pack() # This has to be used if we use the
                                                                          #destroy()

window.mainloop()
#old_window.mainloop() # This has to be used if we use the destroy()