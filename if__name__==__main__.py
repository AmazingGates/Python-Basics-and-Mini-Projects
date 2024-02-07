# If __name__=='__main__' - In this section, we will be going over the purpose of the if __name__=='__main__'
# By using the if __name__=='__main__', we can check to see if the user is running the program as a standalone 
#or if they are importing it from another module

# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variable of '__main__' if it's the initail module being run

def main():
    print("Hello")


if __name__=='__main__':
    main()

print(__name__) # This is how to check if the program being run is the __main__, or if it was imported

# Here is another way to check if we are running main or import

if __name__=='__main__':
    print("This Is The Main")

else:
    print("This Is An Import")


# Here is an example on how to run a function in '__main__'
    
def hello():
    print("Hello")

if __name__=='__main__': # This hello() is only set to run if the program is running in main
    hello()