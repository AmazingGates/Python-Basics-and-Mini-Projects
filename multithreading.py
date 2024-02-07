# Multi Threading - A flow of execution. Like a separate order of instructions
# However each thread takes a turn running to achieve concurrency
# GIL (Global interpreter lock) - Allows only one thread to hold the control of the Python interpreter at any one time

# CPU - Program/task spends most of its time waiting for internal events (cpu intensive), uses multiprocessing, 

# IO Bound -Program/ Task spends most of its time waiting for external events (user input, web scraping), uses
#multithreading

import threading, time

#print("------------------------------------------------------------------------")
#print("------------------------------------------------------------------------")

#print(threading.active_count()) # This is the formula to check the active count of threeads running in our program
#print(threading.enumerate()) # This formula will print a list of all the threads running

#print("------------------------------------------------------------------------")
#print("------------------------------------------------------------------------")

def eat_breakfast():
    time.sleep(3)
    print("Breakfast Was Delicious!")


def drink_coffe():
    time.sleep(4)
    print("The Coffe Was Strong!")


def study():
    time.sleep(5)
    print("Practice Makes Perfect!")


#eat_breakfast()

#print("------------------------------------------------------------------------")
#print("------------------------------------------------------------------------")


#drink_coffe()

#print("------------------------------------------------------------------------")
#print("------------------------------------------------------------------------")


#study()

#print("------------------------------------------------------------------------")
#print("------------------------------------------------------------------------")

# In the section below, we will be going over the process of using multithreading, which will allow us to 
#run more than one thread at once.
    

x = threading.Thread(target=eat_breakfast, args=())
x.start()


y = threading.Thread(target=drink_coffe, args=())
y.start()


z = threading.Thread(target=study, args=())
z.start()

#x.join() # This is function we use when we want one function to wait until another function is done before it starts
         # running. In these cases, x, y, and z will run before our main thread can move on with the rest of the program
#y.join()

#z.join()

print(threading.active_count()) # This is the function to check the active count of threeads running in our program
print(threading.enumerate()) # This function will print a list of all the threads running
print(time.perf_counter()) # This function allows us to see how long it takes our main thread to finish its thread