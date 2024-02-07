# Drag & Drop - In this section we will be going over the process of dragging and dropping widgets

from tkinter import *

def drag_start(event):
    widget = event.widget # This allows to make our function compatiable with all our widgets. Also widget = event.wiget
    #will get the widget of our event and temporarily rename it to widget (widget = event.widget)
    widget.startX = event.x # This gives us the coordinates of where we click within our label
    widget.startY = event.y # This gives us the coordinates of where we click within our label


def drag_motion(event):
    widget = event.widget # This allows to make our function compatiable with all our widgets. Also widget = event.wiget
    #will get the widget of our event and temporarily rename it to widget (widget = event.widget)
    x = widget.winfo_x() - widget.startX + event.x # "x = widget.winfo_x()" will get the top left x coordinate of our 
#label relative to the window that we are in. "widget.startX" is the place where we click witin the label itself
# "event.x" is where we start dragging our widget to. Combinning all 3 together will give us the coordinates of where
#we want to drag our widget
    y = widget.winfo_y() - widget.startY + event.y # "y = widget.winfo_y()" will get the top left x coordinate of our 
#label relative to the window that we are in. "widget.startY" is the place where we click witin the label itself
# "event.y" is where we start dragging our widget to. Combinning all 3 together will give us the coordinates of where
#we want to drag our widget
    widget.place(x=x ,y=y) # By using the x=x and y=y inside our place() allows us to drag and drop our widget 
#where we choose.


window = Tk()


label = Label(window,bg="red",width=10,height=5)
label.place(x=0,y=0) # The place() allows us to pick our labels starting location by setting its x and y coordinates

label2 = Label(window,bg="blue",width=10,height=5)
label2.place(x=100,y=100) # The place() allows us to pick our label2 starting location by setting its x and y coordinates


label.bind("<Button-1>",drag_start) # The bind() allows us to bind widgets by using the widgets name (label) and the
#bind(). The bind() can take two arguments, an (event) and a (function). bind(event,function name). 
# "<Button-1>" implies that we want the mouse left button click to be the trigger that calls our function
label.bind("<B1-Motion>",drag_motion) # The bind() allows us to bind widgets by using the widgets name (label) and the 
#bind(). The bind()takes can take two arguments, an (event) and a (function). bind(event,function name).
# "<B1-Motion>" = to holding down the left mouse button and dragging. "<B1-Motion>" gives us the ability to drag 
#items we choose across our window 

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)


window.mainloop()