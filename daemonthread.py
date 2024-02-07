# Daemon Thread - A thread that runs in the background, not important for program to run
# Your program will not wait for daemon threads to complete before exiting
# Non-daemon threads cannot normally be killed, they stay alive until task is complete

# ex. background tasks, garbage colection, waiting for input, long running processes

import threading, time


def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")


x = threading.Thread(target=timer, daemon=True) # This is the method to change a thread to daemon thread
x.start()

#x.setDaemon(True) # This is the method to change a daemon to a non daemon or vice versa. The action
                   #can only be preformed before the daemon is run. It cannot be changed while it's running

#print(x.isDaemon()) # This method will allow us to check if a thread is a daemon or not


answer = input("Do You Wish To Exit? ")