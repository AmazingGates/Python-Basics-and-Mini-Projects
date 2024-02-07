# Write A File - In this section we will be going over the process of writing a file.
text = "\nCASA DE GATES" # Just a reminder, use the new line function (\n) when appending new items to your file
                           # This will make sure the new item is entered on a new line and not on a previuos items line

with open("test.txt", "a") as file: # When we want to write a file we enter "w" as the second argument in the open()
    file.write(text)                # Using just the "w" argument will write a file, and it will also overwrite any
                                    #existing data already in the file.
                                    # To add things to our file without having to erase the previous items, we can
                                    #use the "a" as the second argument to append the items to our list. This method
                                    #will ensure that we not only add items to our file, but we also keep what we 
                                    #previously had in the file, if we choose.                