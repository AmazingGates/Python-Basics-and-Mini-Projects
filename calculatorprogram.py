# Calculator Program - In this section we will be going over the process of creating a basic calculator in Python

from tkinter import *

def button_press(num): # Here we created our and defined our functions
    global equation_text
    equation_text = equation_text + str(num) # This will convert any number we receive into string
    equation_label.set(equation_text) #equation_label is a StringVar and will be set to our equation_text

def equals():
    global equation_text
    try:
        total = str(eval(equation_text)) # eval will parse the expression that we pass in
        equation_label.set(total) # Here we are setting our equation_label to display whatever total is
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Arithmetic Error") # Here we are setting our equation_label to display
        #a custom message if we catch a ZeroDivisionError 
    except SyntaxError:
        equation_label.set("Syntax Error") # Here we are setting our equation_label to display
        #a custom message if we catch a SyntaxError   

def clear():
    global equation_text
    equation_label.set("") # This is how we set our equation_label to clear, and clear our calculator window
    equation_text = "" # This is how we set our equation_text to clear, and display a blank window

window = Tk() # This is how we created our window
window.title("Calculator Program") # This is how we give our window a title
window.geometry("500x500") # This is how we set the dimensions of our window

equation_text = ""

equation_label = StringVar()

label = Label(window,textvariable=equation_label,font=("Italic",21),bg="white",width=24,height=3) # This is how we
#created and defined a label
#in our window
label.pack() # We display our label in our window by (pack()) packing it on.

# Here we will create a frame for all the buttons we create.
frame = Frame(window) # This is how we create our frame
frame.pack() # This is how we display our frame in our window

button1 = Button(frame, text=1, height=4, width=9,font=36,command=lambda:button_press(1)) # This is how we
#create, add to our frame, and define our buttons
button1.grid(row=0,column=0) # This is how we add our button and place it where we want it in our grid
button2 = Button(frame, text=2, height=4, width=9,font=36,command=lambda:button_press(2)) # This is how we
#create, add to our frame, and define our buttons
button2.grid(row=0,column=1) # This is how we add our button and place it where we want it in our grid
button3 = Button(frame, text=3, height=4, width=9,font=36,command=lambda:button_press(3)) # This is how we
#create, add to our frame, and define our buttons
button3.grid(row=0,column=2) # This is how we add our button and place it where we want it in our grid
button4 = Button(frame, text=4, height=4, width=9,font=36,command=lambda:button_press(4)) # This is how we
#create, add to our frame, and define our buttons
button4.grid(row=1,column=0) # This is how we add our button and place it where we want it in our grid
button5 = Button(frame, text=5, height=4, width=9,font=36,command=lambda:button_press(5)) # This is how we
#create, add to our frame, and define our buttons
button5.grid(row=1,column=1) # This is how we add our button and place it where we want it in our grid
button6 = Button(frame, text=6, height=4, width=9,font=36,command=lambda:button_press(6)) # This is how we
#create, add to our frame, and define our buttons
button6.grid(row=1,column=2) # This is how we add our button and place it where we want it in our grid
button7 = Button(frame, text=7, height=4, width=9,font=36,command=lambda:button_press(7)) # This is how we
#create, add to our frame, and define our buttons
button7.grid(row=2,column=0) # This is how we add our button and place it where we want it in our grid
button8 = Button(frame, text=8, height=4, width=9,font=36,command=lambda:button_press(8)) # This is how we
#create, add to our frame, and define our buttons
button8.grid(row=2,column=1) # This is how we add our button and place it where we want it in our grid
button9 = Button(frame, text=9, height=4, width=9,font=36,command=lambda:button_press(9)) # This is how we
#create, add to our frame, and define our buttons
button9.grid(row=2,column=2) # This is how we add our button and place it where we want it in our grid
button0 = Button(frame, text=0, height=4, width=9,font=36,command=lambda:button_press(0)) # This is how we
#create, add to our frame, and define our buttons
button0.grid(row=3,column=1) # This is how we add our button and place it where we want it in our grid
plus = Button(frame, text="+", height=4, width=9,font=36,command=lambda:button_press("+")) # This is how we
#create, add to our frame, and define our buttons
plus.grid(row=0,column=3) # This is how we add our button and place it where we want it in our grid
minus = Button(frame, text="-", height=4, width=9,font=36,command=lambda:button_press("-")) # This is how we
#create, add to our frame, and define our buttons
minus.grid(row=1,column=3) # This is how we add our button and place it where we want it in our grid
multiply = Button(frame, text="*", height=4, width=9,font=36,command=lambda:button_press("*")) # This is how we
#create, add to our frame, and define our buttons
multiply.grid(row=2,column=3) # This is how we add our button and place it where we want it in our grid
divide = Button(frame, text="/", height=4, width=9,font=36,command=lambda:button_press("/")) # This is how we
#create, add to our frame, and define our buttons
divide.grid(row=3,column=3) # This is how we add our button and place it where we want it in our grid
equal = Button(frame, text="=", height=4, width=9,font=36,command=equals) # This is how we
#create, add to our frame, and define our buttons
equal.grid(row=3,column=2) # This is how we add our button and place it where we want it in our grid
decimal = Button(frame, text=".", height=4, width=9,font=36,command=lambda:button_press(".")) # This is how we
#create, add to our frame, and define our buttons
decimal.grid(row=3,column=0) # This is how we add our button and place it where we want it in our grid
clear = Button(window, text="clear", height=4, width=9,font=36,command=clear) # This is how we
#create, add to our frame, and define our buttons
clear.pack()

window.mainloop()