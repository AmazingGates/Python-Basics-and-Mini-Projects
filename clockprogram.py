# Clock - In this section we will be creating a Clock Program

from tkinter import *
from time import *


def update(): # This is where we will create and define our update().
    time_string = strftime("%I:%M:%S %p") # strftime will convert a tuple or a struct_time representing a time as returned by
    #gmtime() or localtime() to a string specified by the format argument. Colons (:) are used to separate
    #the values for a better visual display
    time_label.config(text=time_string) # This will display the current time in style we specified with our
    #directives


    day_string = strftime("%A")
    day_label.config(text=day_string)
    # These are some of the directives that we can pass as arguments into our function
    # %A = Locale's full weekday name


    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)
    # These are some of the directives that we can pass as arguments into our function
    # %B = Locale's full month name
    # %d = Day of the month as a decimal number [01,31]
    # %Y = Year with century as a decimal number




    window.after(1000,update) # This is how we update our clock program using the .after()
    # (1000,update) = Will call back and update our update() every 1 second (1000) using the update
    #call back

    # These are some of the directives that we can pass as arguments into our function
    # %I = Hour(12-hour clock) as a decimal number [01,12]
    # %M = Minute as a decimal number [00,59]
    # %S = Second as a decimal number [00,61]
    # %p = Locale's equivalent of either AM or PM



window = Tk()


time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black") # This is how we create and define our time window
time_label.pack() # This is how we display our time window inside our GUI

day_label = Label(window,font=("InK Free",25)) # This is how we create and define our day window
day_label.pack() # This is how we display our day window inside our GUI

date_label = Label(window,font=("Arial",30)) # This is how we create and define our date window
date_label.pack() # This is how we display our date window inside our GUI


update() # This will update the time in our Clock Program


window.mainloop()