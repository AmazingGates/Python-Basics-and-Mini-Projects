# Multiple Animations - In this section we will be going over the process of creating Multiple Animations on 
#our canvas

# We will also be creating our own class to import over and use in our code. (class Ball)

from tkinter import *
import time
from Ball import * # This is how we import our class Ball and import everything from it



window = Tk()


WIDTH = 500 # These will be used as constant to keep the shape of our canvas
HEIGHT = 500 # These will be used as constant to keep the shape of our canvas

canvas = Canvas(window,width=WIDTH,height=HEIGHT,background="gold") # This is how we create and define our canvas.
canvas.pack() # This is how we display our canvas to our window

volley_ball = Ball(canvas,0,0,100,1,1,"red") # This is how we construct and define the Ball() according to
#the parameters set in our class Ball. Each parameter the Ball() takes corresponds to a parameter set in our
#def __init__(self)

tennis_ball = Ball(canvas,0,0,50,4,3,"black") # This is how we construct and define the Ball() according to
#the parameters set in our class Ball. Each parameter the Ball() takes corresponds to a parameter set in our
#def __init__(self)

basket_ball = Ball(canvas,0,0,125,8,7,"green") # This is how we construct and define the Ball() according to
#the parameters set in our class Ball. Each parameter the Ball() takes corresponds to a parameter set in our
#def __init__(self)


while True: # This is how we add movement for all our balls
    volley_ball.move() # This will move our volley ball while the program is running by calling the move()
    #from our class Ball module.
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()