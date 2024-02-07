# Message Box - In this section we will be creating a message box and using different functions to program it

from tkinter import *
from tkinter import messagebox # This imports the messagebox library

def click(): # This are the different messageboxes we can use with this function
     #messagebox.showinfo(title="To The Princess",message="I Love You Alia Marie Gates!")
    #messagebox.showwarning(title="WARNING",message='"I DO" MEANS FOREVER')
    #messagebox.showerror(title="ERROR",message="Don't Ask To Have Lasagna For Dinner!")

   if messagebox.askokcancel(title="Question", message="Can We Have A Girlfriend?"):
      print("Anything For You Papi.")
   else:
      print("Maybe next Year.")
    
   # if messagebox.askretrycancel(title="Question", message="I'm Going Out To Have A Drink With The Guys?"):
   #print("Laughing My Ass Off!")
   # else:
    #  print("Duh..., You Better Hit That Cancel Button...")

    #if messagebox.askyesno(title="Question", message="Do You Love Bam Bam Javelle?"):
    #   print("Of Course Papi.")
    #else:
    #   print("Can't Cancel That One Papi!")

    #if messagebox.askquestion(title="Yes or No", message="Will You Be Able To Stand Under My Pressure?"):
    #    print("If Not Me Then Who.")

    #print(messagebox.askquestion(title="Yes or No", message="Will You Be Able To Stand Under My Pressure?"))

    #answer = messagebox.askquestion(title="Yes or No", message="Will You Be Able To Stand Under My Pressure?")
    #if(answer == "yes"):
        #print("If Not Me, Then Who.")
    #else:
        #print("No Isn't An Option!")
    
    #answer = (messagebox.askyesnocancel(title="Last Question",message="Are You Going To Enjoy Us?"))
    #if(answer==True):
    #    print("With All My Heart...")
    #elif(answer==False):
    #   print("Don't Ask Dumb Questions.")
    #else:
    #    print("I Can't Wait To Show You!")

     


window = Tk()    

button = Button(window,
                command=click,
                text="Click Me")


#button.config(command=click)
#button.config(text="Click Me")

button.pack()

window.mainloop()