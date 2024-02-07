# Index Operator [] - Gives access to sequence's elements. They include, but are not limited to (str,list,tuples)
# First we will deal with strings
name = "brian Gates"

if (name[0] or name[6].islower()): # This method checks if the first letter of our string is lowercase, and if it is,
    name = name.capitalize() #it Capitalizes it
print(name)


first_name = name[0:3].upper() # With this method we specified a range of 0-3 of characters we want to return.
print(first_name)

last_name = name[6:].capitalize() # With this method we were able to return only our last name, and make sure it is
print(last_name)                  #Capitalized
