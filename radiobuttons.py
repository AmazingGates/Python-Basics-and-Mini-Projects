# Radio Buttons - Similar to check boxes/buttons, but you can only select one from a group

from tkinter import *

food = [
    "Pizza",
    "Hamburger",
    "Steak"
]

def order(): # This is the function we set to run when our buttons are pushed
    if(x.get()==0):
        print("You ordered the Pizza!")
    elif(x.get()==1):
        print("You ordered the Hamburger!")
    elif(x.get()==2):
        print("You ordered the Steak!")
    else:
        print("Please order from the menu.")

window = Tk()

pizzaImage = PhotoImage(file="Alia 33.png")
hamburgerImage = PhotoImage(file="Alia 33.png")
steakImage = PhotoImage(file="Alia 33.png")

foodImages= [pizzaImage, hamburgerImage, steakImage]

x = IntVar()

for index in range(len(food)): # This is how we iterate through our food list/[]
    radiobutton = Radiobutton(window, # This is how we create our Radio Button and give it its instances
                              text=food[index],
                              variable=x, 
                              value=index, 
                              padx=25,
                              font=("impact",60), 
                              #image=foodImages[index], 
                              compound="right", 
                              indicatoron=0,
                              width=375,
                              command=order) 
    #radiobutton.config(text=food[index]) # Add stext to radio buttons We can also control the features of our radio button here,
    #radiobutton.config(variable=x)       # Groups buttons together if they share the same variable
    #radiobutton.config(value=index) # This assigns each button a different value
    #radiobutton.config(padx=25) # This adds padding to our x-axis
    #radiobutton.config(font=("impact",30)) # This changes text font and text size
    #radiobutton.config(image=foodImages[index]) # allows us to add images to our radio buttons
    #radiobutton.config(compound="right") # Allows us to add image And text to our buttons
    #radiobutton.config(indicatoron=0) # This allows us to remove the button hole from our buttons, changes buttons to push buttons
    #radiobutton.config(width=375) # This allows us to set the width of our buttons
    #radiobutton.config(command=order) # This allows us to set command of radio button to our function

    radiobutton.pack(anchor="w") # This is how we display our radio button in our GUI/window. By passing in the 
                                 #anchor="w" into our pack(), we can position our buttons to the "west" of the window

window.mainloop()