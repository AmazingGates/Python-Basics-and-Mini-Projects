# Read A File - In this section we will be going over the process of rading a file.

with open('test.txt') as file: # This is how we select which file we want to read. Also, on a side note, since the file
    print(file.read())         #is already in our folder, we don't need to add a path. If the file was outside of folder,
                               #we would need a path to access the file.
                               # Also, using the with open() will automatically close the file once it is done.

print(file.closed) # This is the method we use when we want to check if a file is open or closed. If closed, print
                   #will return True. If the file is left open, the print will return False.


# In the example elow we will be solving the same problem above but this time we will be using a Try and Except
try:
    with open("test.txt") as file: # Using a try and except lets us catch errors we may encounter when 
        print(file.read())         #looking for a file
except FileNotFoundError:
    print("That File Was Not Found!")