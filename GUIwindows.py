# GUI Windows - In this section, we will be creating our very own Graphical User Interface

from tkinter import * # With the tkinter import, we have access to all the functions and features of the GUI module

# Widgets - GUI elements: buttons, textboxes, labels, images
# Windows - Serves as a container to hold or contain these widgets

# In the example below, we will be creating our own Window
# All of the window() should appear betwwen (window = TK and window.mainloop)

window = Tk() # This function instantiates an instance of a window for us
window.geometry("300x300") # This function chabges the size of our GUI
window.title("Para La Casa De Gates!") # This function allows us to change the title of our GUI
icon = PhotoImage(file="Alia 33.png") # This is how we change the icon on our GUI
window.iconphoto(True, icon) # This is how we apply the icon change to our GUI
window.config(background="red") # This function allows us to make changes to our window ie = color
photo = PhotoImage(file="Alia 33.png") # This is how we change the icon on our GUI

label = Label(window,
              text="LONG LIVE GATES!!!", 
              font=("sans serif",30,"bold","underline"),
              fg="green",
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound="right")


label.pack()

window.mainloop()# This function will display our window, and listen for events