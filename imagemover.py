# Image Mover - In this section we will be going over the process of moving an image on both
#a Window and a Canvas
# This will be a 2 part exercise. First we will go over the process of moving a wideget in our window


from tkinter import *


def move_up(event): # All event functions must have the event arguement
    label.place(x=label.winfo_x(), y=label.winfo_y() - 10) # x=label.winfo_x() gives us the position our image is
    #currently in relative to the window that it is in
    # 10 allows us to choose the speed at which our image moves up our y axis. We can set this speed 
    #manually by substracting the number from our y=label.winfo_y(). y=label.winfo_y() - 10)

def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 10) # x=label.winfo_x() gives us the position our image is
    #currently in relative to the window that it is in
    # 10 allows us to choose the speed at which our image moves down our y axis. We can set this speed 
    #manually by adding the number to our y=label.winfo_y(). y=label.winfo_y() + 10)

def move_left(event):
    label.place(x=label.winfo_x() - 10, y=label.winfo_y()) # x=label.winfo_x() gives us the position our image is
    #currently in relative to the window that it is in
    # 10 allows us to choose the speed at which our image moves left across our x axis. We can set this speed 
    #manually by substracting the number from our x=label.winfo_x. x=label.winfo_x() - 10)


def move_right(event):
    label.place(x=label.winfo_x() + 10, y=label.winfo_y()) # x=label.winfo_x() gives us the position our image is
    #currently in relative to the window that it is in
    # 10 allows us to choose the speed at which our image moves right across our x axis. We can set this speed 
    #manually by adding the number to our x=label.winfo_x(). x=label.winfo_x() + 10)

    



window = Tk()
window.geometry("500x500") # This is how we set the geometry of our window

window.bind("<w>",move_up) # This is how we bind our keys to functions. Here, we are binding the w key "<w>", 
#to our move_up function
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

window.bind("<Up>",move_up) # This is how we bind our keys to functions. Here, we are binding our arrow keys
#to our functions instead of characters, but it will carry out the same action
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

myimage = PhotoImage(file="Alia 33.png")
label = Label(window,image=myimage) # We can use a subsitute for an image with bg="red", or whatever color you want, 
#if we don't have an image to use at the moment
label.place(x=0,y=0) # place() allows us to set the coordinates of our images starting position. Using the x=0
#and the y=0 places our image or color substitue in the upper left hand corner of our window



window.mainloop()
         

