# Checkbox - In this section we will create and customize our own check boxes

from tkinter import *

def display():
    if(x.get()==1):
        print("------------------------------------------------------------------")
        print("If You Want To Keep An Idiot Entertained, UnCheck The Box!")
        print("------------------------------------------------------------------")
    else:
        print("------------------------------------------------------------------")
        print("If You Want To Keep An Idiot Entertained, Follow The Instructions On The Big Bright Sign.")
        print("------------------------------------------------------------------")

window = Tk()

x = IntVar()
#x = BooleanVar() # This is the function we would use if we wanted to use a true or false for our on/off values
#x = StringVar() # This is the function we would use if we wanted to use strings/text for our on/off value

brolly_photo = PhotoImage(file="Alia 33.png")

check_button = Checkbutton(window, # This is how we construct our check box/button by addind in its destination, features and dimensions
                           text="If You Want To Keep An Idiot Entertained, Check This Box!",
                           variable=x,
                           onvalue=1, # This is the value when the button is toggled on
                           offvalue=0, # This is the value that is stored when toggled off
                           command=display,
                           font=("Aerial",30),
                           fg="seagreen",
                           bg="gold",
                           activeforeground="seagreen",
                           activebackground="gold",
                           padx=25,
                           pady=10,
                           #image=brolly_photo,
                           compound="right")

check_button.pack()
window.mainloop()