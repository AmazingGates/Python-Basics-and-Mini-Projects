# Menu Bar - In this section we will be creating a menu bar

from tkinter import *

def openFile():
    print("This File Is Now Open")

def saveFile():
    print("This File Has Been Saved")

def cut():
    print("This File Has Been Cut!")

def copy():
    print("This File Has Been Copied!")

def paste():
    print("This File Has Been Pasted!")



window = Tk()

openImage = PhotoImage(file="")
saveImage = PhotoImage(file="")
exitImage = PhotoImage(file="")

menubar = Menu(window) # This is how we create our menubar
window.config(menu=menubar) # This is how we configure our window the that menubar is displayed

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15)) # This format will add a file inside our menubar window. Also
                                   #the tearoff=0 feature will remove dashed line from above our drop down menu
menubar.add_cascade(label="File",menu=fileMenu) # This function will create a drop down menu for options

fileMenu.add_command(label="Open",command=openFile,image=openImage,compound="left") # These will be our options in the drop down menu. openFile is our callback
fileMenu.add_command(label="Save",command=saveFile, image=saveImage,compound="left") # These will be our options in the drop down menu
fileMenu.add_separator() # This function will separate the other functions above and below
fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound="left") # These will be our options in the drop down menu. "quit" will
                                                #automatically close our file so it doesn't need a function


editMenu = Menu(menubar,tearoff=0,font=("MV Boli",15)) # This format will add an edit inside our menubar window. Also
                                   #the tearoff=0 feature will remove dashed line from above our drop down menu
menubar.add_cascade(label="Edit",menu=editMenu) # This function will create a drop down menu for options

editMenu.add_command(label="Cut",command=cut) # These will be our options in the drop down menu. openFile is our callback
editMenu.add_command(label="Copy",command=copy) # These will be our options in the drop down menu
editMenu.add_separator() # This function will separate the other functions above and below
editMenu.add_command(label="Paste",command=paste)

window.mainloop()