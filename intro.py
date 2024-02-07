# Variable - A container for a value. Behaves as the value it contains.

first_name = "Brian"
last_name = "Gates"
full_name = first_name + " " + last_name
#print(type(full_name)) # We use the type() to check the values classification. (print(type(full_name)))
print("Hello", full_name)


age = 37
age += 1
print("You are" + " " + str(age)) # Since we can't concaternate stings and integers naturally, using this step helps
#us do so.
#print(type(age))


# float - A floatint point number (A decimal number)
height = 6.0
print("Your height is" + " " + str(height) +"ft tall")
#print(type(height))


# boolean - A variable that only store True or False
human = True
print("Are you a Human:" + " " + str(human))
#print(type(human))