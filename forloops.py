# For Loop - A statement that will execute it's block of code for a limited amount of times.
for i in range(10):
    print("Long Live Gates")


for i in range(50, 101): # In this example we started our loop at 50 (which is inclusive) and stopped at 100
    print(i)             #because 101 is (exclusive)


for i in range(50, 100, 3): # In this example we used a 3rd parameter to tell the code that we only want
    print(i)                #to count every third character of the values starting from 50 and ending at 100.


for i in "Brian Javelle Gates": # This is the method to iterate over a string. Reminder (even the spaces in 
    print(i)                    #the string get iterated over and returned, unless tiold other wise.)

    