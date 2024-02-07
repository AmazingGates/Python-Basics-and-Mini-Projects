# Canvas - Widget that is used to draw graphs, plots, and images in a window
# When using Canvas, the most recent items will overlap the previous items. Just an FYI

from tkinter import *



window = Tk()


canvas = Canvas(window,height=500,width=500) # This is how we create our canvas and set its features
#canvas.create_line(0,0,500,500,fill="red",width=5) # This is how we create a line on our canvas. (0,0) = (top left)
#is our starting location. (500,500) = (bottom right) is our ending position
#canvas.create_line(0,500,500,0,fill="black",width=5) # This is another line we creatated on our canvas. For our 
#black line, our strarting "x" position is (0) and our starting "y" position is (500). Next our ending "x" location
#(500) and our ending "y" position will be (0). This will have our black line go from bottom left to top right
#canvas.create_rectangle(50,50,250,250,fill="purple") # This is how we add a rectangle shape to our canvas
#points = [250,0,500,500,0,500] # We created a list called points that we can add to our items via list name (points)
# Our points list contains the coordinates our item will have
#canvas.create_polygon(points,fill="yellow",outline="black",width=5) # This is how we add a polygon shape to our canvas
# outline= is how we add a border to our item
#canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,width=5) # This is how we add an arc shape to our canvas
# start= allows us to choose where our items starting position will be. Also start= moven will be interpreted as 
#degress of a circle
canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10) # extent allows to dictate how far our item extends
canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
canvas.create_oval(190,190,310,310,fill="white",width=10)
canvas.pack()


window.mainloop()