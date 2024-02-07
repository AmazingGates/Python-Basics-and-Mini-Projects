# List Box - A listing of selectable text items within it's own container

from tkinter import *

def submit(): # This is where we define our submit function

    food = []

    for index in listbox.curselection(): # This for loop will iterate over each item we select, so we may target
                                         #them all at once
        food.insert(index,listbox.get(index))

    print("You have ordered: ")
    for index in food: # This for loop will allow us to print out everything we selected, so we may target them all
        print(index)


def add(): # This is where we define our add function
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def delete():
    for index in reversed(listbox.curselection()): # This for loop will allow us to iterate over multiple items at once for 
        listbox.delete(index)            #deletion
    listbox.config(height=listbox.size())


window = Tk() # This is how we open a window/GUI

listbox = Listbox(window,
                  bg="wheat",
                  font=("Aerial",36),
                  width=30
                  )
listbox.pack()

listbox.insert(1,"Steak") # This is the function we use to insert the items into their location on our menu
listbox.insert(2,"Egg")
listbox.insert(3,"Cheese")
listbox.insert(4,"Cinnamon Raisin Bagel")
listbox.insert(5,"Cream Cheese")

#listbox.config(bg="wheat")
#listbox.config(font=("Aerial",36))
#listbox.config(width=15)
listbox.config(height=listbox.size()) # This size function allows us to scale the height of our listbox dynamically
                                      #Meaning that our menu will shrink and grow with the items added or removed
listbox.config(selectmode=MULTIPLE) # This feature allows us to change our select rate to MULTIPLE



entryBox = Entry(window)
entryBox.pack()


submitButton = Button(window,
                      text="Submit",
                      command=submit)
submitButton.pack()

addButton = Button(window,
                      text="Add",
                      command=add)
addButton.pack()

deleteButton = Button(window,
                      text="Delete",
                      command=delete)
deleteButton.pack()


window.mainloop() # All the code for the GUI/window must be above this mainloop()