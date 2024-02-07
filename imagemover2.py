# Image Mover - In this section we will be going over the process of moving an image on both
#a Window and a Canvas
# This wwas a 2 part exercise. In part 2, we are going over the process of moving a widget on our canvas

# Hint: Make sure to add the backgound first depending on its size, it may block the othe rimages from view


from tkinter import *


def move_up(event): # We can use the canvases move() to move an image a certain amount of pixels on the x axis 
    #and y axis
    canvas.move(myimage,0,-10) # The move() takes 3 arguments. First is the we want to use (myimage). x
    #Second is the amount of pixels we want to move it on the x axis(myimage,0). Third will be the amount 
    #of pixels we want to move it on the y axis (myimage,0,10) (0) will keep the image nuetral on the x axis while
    #in motion. (-10) will move the image 10 pixels spaces up the y axis when in motion

def move_down(event):
    canvas.move(myimage,0,10) # (0) will keep the image nuetral on the x axis while in motion. (-10) will move 
    #the image 10 pixels spaces down the y axis when in motion

def move_left(event):
    canvas.move(myimage,-10,0) # (-10) will move the image 10 pixels to the left on the x axis while in motion.
    #(0) will kee the image nuetral on the y axis while in motion

def move_right(event):
    canvas.move(myimage,10,0) # (+10) will move the image 10 pixels to the right on the x axis while in motion.
    #(0) will kee the image nuetral on the y axis while in motion




window = Tk()

window.bind("<w>",move_up) # This is how we bind our keys to functions
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

window.bind("<Up>",move_up) # This is how we bind our arrow keys to functions
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)


canvas = Canvas(window,width=500,height=500)
canvas.pack()

photoimage = PhotoImage(file="Alia 1.png") # This is how we add an image to our widget
myimage = canvas.create_image(0,0,image=photoimage,anchor=NW) # This is how we set the coordinates of our
#images initial starting location. (0,0) indictaes that we want the image set in the top left corner by 
#placing a 0 in both the x, and y coordinates
# Using the ancor=NW feature allows us to bring our image into frame and anchors it in the NW coordinates of the
#canvas
window.mainloop()