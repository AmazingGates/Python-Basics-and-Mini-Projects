# MultiProcessing - Running task in parallel on different cpu cores, bypasses GIL used for thread
#                   Better for gpu bound tasks (heavy cpu usage)
# Multithreading - Better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num): # This is an example of a function that is programmed to count by one to a predertermined number
    count = 0
    while count < num:
        count += 1

def main():
    
    #print(cpu_count()) # By printing whatever this function returns, we can get the count of the number of
                       #additional processes we can run
    a = Process(target=counter, args=(250000000,)) # This is an example of a Process(). Remember, the target is 
                                                 #our funnction (counter()), which gets targeted like this
                                                    #(target=counter). Also, the args takes a tuple(). If you
                                                    #don't have a second argument, put a comma after your first
                                                    #to imply that there are 2 argument spaces being used ex.
                                                    #(args=(1000000000,))
    
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))# By adding even more Processes we can spread out load even more
    d = Process(target=counter, args=(250000000,))

    a.start() # This is how we start our Process()
    b.start() # How intial number was 1 billion for Process a. But since we added a second Process, we were able
              #to divide the load between the 2 Processes and cut down its run time.
    c.start() # Now that we 4 Process, we split the 1 billion into 4 sets of 250 million
    d.start() # This will cut the run time down even more
 
    a.join() # This is a process for syncronization. The main process will wait around for the child process to finish
    b.join()
    c.join()
    d.join()



    print("Finished in: ", time.perf_counter(), "seconds")


if __name__=="__main__":
    main()