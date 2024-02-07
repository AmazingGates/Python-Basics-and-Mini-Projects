# Delete A File - In this section we will be going over the process of deleting a file.
import os
import shutil

#os.remove("copy.txt") # This is the method we use to delete a file

# In the example below we will run the same code as above, but wrap it in a try and except this time
# This helps us in case we attempt to delete a file that is not there.
# This function does work on Empty Folders. There is a different function for that and we dicuss it below
#try:
 #   os.remove("Empty Folder")
  #  print("File Removed")
#except FileNotFoundError:
 #   print("That File Was Not Found")


# In the example below we will go over the process of deleting an empty folder
#try:
 #   os.rmdir("Empty Folder") # This is the function we use to delete an empty folder, and will not work on folders
  #                        #that have files. There is a different function for that and we dcuss it below
#except FileNotFoundError:
 #   print("File Not Found")
#except PermissionError:
 #   print("You Don't Have Permission For This Action")
#else:
 #   print("Folder Removed")


# In this section we will be going over the steps of deleting a folder with fils in it
try:
    shutil.rmtree("New Shit Folder") # This is the process we use to delete folders with files. must import the  
except FileNotFoundError:            #shutil module to use this function
    print("File Not Found")
except PermissionError:
    print("You Don't Have Permission For This Action")
except OSError:
    print("Not The Right Function For This Process/Folder Has Files")
else:
    print("Folder Removed")