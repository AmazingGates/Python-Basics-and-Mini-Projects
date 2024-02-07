# Progress Bar - In this section we will be creating A Progress Bar to track the status of a download

from tkinter import *
from tkinter.ttk import * # ttk is the module where the Progressbar function can be found
import time

def start():
    GB = 100
    download = 0
    speed = 1
    while(download<GB): # This while loop will fill our bar immediately so we added a time.sleep() 
                   #put some space between initialization and completion
        time.sleep(0.05) # This is time delay we added. It is set for 0.05 second intervals
        bar["value"]+=(speed/GB)*100 # This is how set the amount of bar filled per iteration
        download+=speed
        percent.set(str(int((download/GB)*100))+"%") # This is how we set what percent is, and the (str()) allows us 
                                #to convert the result to a string, but first will cast everything to an int so we can
                                #display whole numbers in our Progress bar (str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB Successfully Downloaded") # This is how we set the
                           #download in our Progress bar. Because we are displaying integers, we have to convert
                           #them to string
        window.update_idletasks() # This function will allow us to refresh the progress bar after each iteration
                                  #and fill it gradually by 10 every 1 second until our bar is filled

    bar["value"] += 10 # This function will fill our Progress bar by 10 each time we click the button



window = Tk()

percent = StringVar() # Using the StringVar() will let us to update our label with text
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentlabel = Label(window,textvariable=percent).pack() # The textvariable= will allows us to update our label
                                                  #with text after each iteration of our while loop
GBlabel = Label(window,textvariable=text).pack()

button = Button(window,text="Download",command=start).pack()

window.mainloop()