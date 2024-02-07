# Open A File (File Dialog) - In this section we will be going over the steps to use a File Dialog
#to open and read a file

from tkinter import *
from tkinter import filedialog

def openFile(): # This is the function we use to access our file path
    filePath = filedialog.askopenfilename(title="File Reader", # This is the function we use to access our file path
                                          filetypes=(("text files","*.txt"), # This function allows us to pick which 
                                          ("all files","*.*")))              #files we want to look for
                                          
    file = open(filePath, "rt") # This is the function we use to read our file. open() takes 2 arguments.
                                #open(filePath, "rt"). ("rt" = read text) and works just like ("r" = read only)
    print(file.read()) # This is how we print the file we want to read
    file.close() # This function will close our file once we are done with them


window = Tk()

button = Button(text="Open",
                command=openFile)

button.config(text="Open")
button.config(command=openFile)

button.pack()

window.mainloop()