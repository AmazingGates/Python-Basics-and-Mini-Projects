# Move A File - In this section we will be going over the steps of moving a file
import os

#source = "test.txt"

source = "New Shit Folder"

#destination = "C:\\Users\\alpha\\OneDrive\\Desktop\\test.txt" # Don't forget to add an addition backslash for every 
                                                              #to cancel any errors.

destination = "C:\\Users\\alpha\\OneDrive\\Desktop\\New Shit Folder" # This method will help us move a Folder instead 
                                                                     #of a file. (Excuse the Folder name, it was just 
                                                                     #for the example)
                                                                     # Also, Folder must exist before you can move it

try:
    if os.path.exists(destination):
        print("There Is Already A File There")
    else:
        os.replace(source, destination) # We use this function in the case a different file is at the location we 
        print(source + " Was Moved")    #are trying to send our file to. This function will replace the original file 
                                        #and place the new file in its place.
except FileNotFoundError:
    print(source + " Was Not Found")