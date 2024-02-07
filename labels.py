# Label - An area widget that holds text and/or an image within a window

from tkinter import *

window = Tk()

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
              compound="right") # We can break our code up like this for easier reading
# This is how we instantiate our label The Label() takes at least 2 arguments
#font= - Changes the font of the text
#30 - is the font size (but we can make it whatever we want)
#bold - tells the program we the font to be bold
#underline - tells the program we want to underline the text
#fg= - allows us to change the color of the text
#bg= - allows us to change the background color of the text
#relief - allows us to add a border to our text
#bd - allows us to change the size of the border
#padx= - allows us to add padding between the text and the border
#pady= - allows us to add padding above and below our text
#image= - allows us to add an image to our label
#Comound= - This is how we add text AND an image to our label

label.pack() # This is the function we use to add our custom label to our GUI window. By default, this function will
             #place our label in the top center location of our window 
#label.place(x=0,y=0) # This function also allows us to put custom labels in our GUI window, but with the place(), 
                      #we can can choose the location we want to place our label

window.mainloop()