# 2d Animations - In this section we will be going over the process of animating an image on a canvas

from tkinter import *
import time


WIDTH = 500 # This Variable is a constant, which means that we do not intend for it to change its value
HEIGHT = 500 # This Variable is a constant, which means that we do not intend for it to change its value
# We created these constants because we will be using them a lot in this code so it's easier to just declare
#them now
xVelocity = 3 # This sets the speed of our ufo on the x axis
yVelocity = 2 # This sets the speed of our ufo on the y axis


window = Tk()


canvas = Canvas(window,width=WIDTH,height=HEIGHT) # This is how we create our canvas and set its dimensions
canvas.pack() # This is how we add our canvas to our window

photo_image = PhotoImage(file="UFO1.png") # This is how we 
#choose which image we want to use on our canvas
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW) # This is how we create/display our image on our 
#canvas. We can also set its x and y starting coordinates (0,0) as well as anchor our image to a pacific region
#(anchor=NW)

background_photo = PhotoImage(file="Space1.png") # This is how we 
#choose which image we want to use on our canvas
background_image = canvas.create_image(0,0,image=background_photo,anchor=NW) # This is how we create/display our image on our 
#canvas. We can also set its x and y starting coordinates (0,0) as well as anchor our image to a pacific region
#(anchor=NW)

image_width = photo_image.width() # This determines the width of our photo image
image_height = photo_image.height() # This determines the height of our photo image

while True:
    coordinates = canvas.coords(my_image) # This will givess us the coordinates of where our image is located
    print(coordinates) # This prints the coordinates to the consoles window. This isn't required, learning only
    if(coordinates[0]>=WIDTH-image_width or coordinates[0]<0): # This allows our ufo to bounce off the wall and and back
        xVelocity = -xVelocity                   #into frame instead of leaving the frame completely
    if(coordinates[1]>=HEIGHT-image_height or coordinates[1]<0): # This allows our ufo to bounce off the wall and and back
        yVelocity = -yVelocity                   #into frame instead of leaving the frame completely
    canvas.move(my_image,xVelocity,yVelocity) # This move() takes 3 arguments (The image name, x coordinates, 
    #y coodinates). This allows us to update our UFO's position
    window.update() # This will update our window for any changes
    time.sleep(0.01) # Our thread which is in charge of running our program will sleep for one one-hundreth of 
    #a second



window.mainloop()