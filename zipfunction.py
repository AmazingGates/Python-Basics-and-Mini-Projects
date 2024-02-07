# Zip(*iterables) Function - Will aggreagate elements from 2 or more iterables (list, tuples, sets, etc.)
# Creates a zip object with paired elements stored in tuples for each element within our zip object

usernames = ["Brian", "Papi", "Gucci"] # This is our dict/[]
passwords = ("javelle", "python", "gates") # This is our tuple/()
login_date = ["1/17/1985", "10/22/1992", "12/25/2024"] # Thisis our list

users = zip(usernames, passwords) # This is how we use the zip() with its parameters. Here, we used the zip() to
                                  #combine elements from the usernames dict/[], and the passwords tuple/().
for i in users:                   # Zip objects iterable
    print(i)
    

# The returned results are stored in a new tuple/() once printed
    
# In the example below we will go over the process of converting a zip() into a dict/[]
    
users = list(zip(usernames, passwords)) # This is how we will convert our zip() into a dict/[] using a dict cast
                                  
for i in users:                   
    print(i)
    print(type(users))


# In the example below we will be going the process to convert our zip() into a dict/[] by using a dict cast
    
users = dict(zip(usernames, passwords)) # This is how we will convert our zip() into a dict/[] using a dict cast
                                  
for key,value in users.items():                   
    print(key+" : "+value)
    print(type(users))

# The returned results are stored in a new dict/[] once printed
    

# In the example below, we will be using our zip() to take 3 iterables, instead of 2.

users = zip(usernames,passwords,login_date)

for i in users:
    print(i)

# We were able to combine 3 iterables in our zip(), and also return elements from all 3 iterables
#in the output from print()