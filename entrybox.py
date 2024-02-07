# Entry Box/Widget - Textbox that accepts a single line of user input

from tkinter import *

def submit(): # This is the function that will be run when our submit callback is clicked
    username = entry.get()
    print("-----------------------------------------------------------------------------")
    print("What's Up " + username + ", you know you the One Right.")
    print("-----------------------------------------------------------------------------")
    entry.config(state=DISABLED) # This function allows us to make our entrybox active or disabled when we want. Using
                                 #it here, our entrybox will be disabled after we enter our text

def delete():
    entry.delete(0, END) # This function allows us to delete what is in our entry box. It also takes at 
                         #least 2 arguments. (0) tells the program to start at the beginning of the string/text
    
def backspace():
    entry.delete(len(entry.get())-1, END) # This is how we program our back space button, which will start at the end
                                        #of our string/text and work its way backwards

window = Tk()

entry = Entry(window, # This is how we create an entry box in our window GUI
              font=("Sans Serif", 60),
              fg="green",
              bg="black")

#entry.insert(0, "Enter Text Here") # This function allows us to add some default text to our entrybox. (Reminder)
                                   # Text has to be removed before you can add your own text with this method
#entry.config(state=DISABLED) # This function allows us to make our entrybox active or disabled when we want. Using
                                 #it here, our entrybox will be disabled after we enter our text

entry.config(show="*") # This function allows us to make our text entries private


entry.pack(side=LEFT) # This is how we display our entrybox in our window/GUI
                      #Also, This method allows us to place on widgets on whatever side we want

submit_button = Button(window,text="submit",command=submit) # This is how we display our submit button
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="delete",command=delete) # This is how we display our delete button
delete_button.pack()

backspace_button = Button(window,text="backspace",command=backspace) # This is how we display our backspace button
backspace_button.pack()

window.mainloop()