# If Statements - A block of code that will execute if it's condition is true. The program only runs the code whose
#conditions have been met. Once those conditions are yet the other statements are ignored and the code continues on.
age = int(input("How old are you? "))

if age > 20:
    print("You are an Adult ")
elif age > 19:
    print("Close,but you are not ready yet")
else:
    print("You are too young to be here ")
    