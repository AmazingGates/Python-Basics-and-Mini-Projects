# File Detection - Checks to see if a file exists somewhere on my computer
import os

path = "C:\\Users\\alpha\\YouTube\\yt.py" # This is a random file from our computer that we are using as an example
if os.path.exists(path): # This is the method we use when we want to check if a certain file path is detected 
                         #on our computer
    print("That Location Exists")
    if os.path.isfile(path): # This is the method we use when we want to check if the path we entered does 
                             #indeed belong to a file
        print("That Is A File")
    elif os.path.isdir(path): # This is the method when we want to check if the path belongs to a Directory
        print("That is a Directory")
else:
    print("That Location Does Not Exist")


