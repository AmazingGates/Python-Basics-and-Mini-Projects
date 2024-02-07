# grid() - Geometry manager that organizes widgets in a table-like structure in a parent 

from tkinter import *



window = Tk()

titleLabel = Label(window,text="Enter Your Info",font=("sans serif", 30)).grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window,text="First Name: ",width=20,bg="red").grid(row=1,column=0) # This is how we create our
#first row and column using the grid(). The grid() also allows us to place widgets where we want in our window using
#the row= and column= features
firstNameLabel = Entry(window).grid(row=1,column=1) # This Entry box location will be the same row as the 
#"First Name", but it will use column 1 instead of 0, placing it to the right of the "First Name" text

lastNameLabel = Label(window,text="Last Name: ",width=20,bg="green").grid(row=2,column=0)
lastNameLabel = Entry(window).grid(row=2,column=1)

emailLabel = Label(window,text="Email: ",width=20,bg="gold").grid(row=3,column=0)
emailLabel = Entry(window).grid(row=3,column=1)

submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2) # Using the columnspan= allows a widget
#to take up more than one slot in our grid()


window.mainloop()