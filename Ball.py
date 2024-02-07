# This class will be used as an import for the multiple animations program

class Ball:

    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color): # This is how construct and define our class Ball
        self.canvas = canvas # This is how we assign all the arguments we will be recieving
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color) # This is how we draw our oval on our canvas
        self.xVelocity = xVelocity # This is related to the direction our oval will initially head in
        self.yVelocity = yVelocity # This is related to the direction our oval will initially head in


    def move(self): # This is where we will define our move()
        coordinates = self.canvas.coords(self.image) # This is how we get our starting point location coordinates
        print(coordinates) # This is how we print those coordinates, but it isn't necessary
        if (coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0): # This is how we set boundaries for our ball to bounce off of
            self.xVelocity = -self.xVelocity # This changes the direction of our ball once it hits the boundary 

        if (coordinates[3]>=(self.canvas.winfo_height()) or coordinates[0]<0): # This will create our top and bottom boundary
            self.yVelocity = -self.yVelocity                             

        self.canvas.move(self.image,self.xVelocity,self.yVelocity) # This is how we define the way our move()
        #moves