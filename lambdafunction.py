# Lambda Function - Functions that are written in 1 line using lambda keyword. Accepts any number of arguments, but
#only has one expression. (Think of it as a shortcut) (Useful if needed for a short period of time, throw-away)

#lambda parameters:expression - This is the syntax for a lambda function

def double(x): # This the "normal" to write this code.
    return x * 2

print(double(5))


#double = lambda x:x * 2 # This is the lambda version of the code above
#multiply = lambda x,y: x * y # This is another example of a lambda function
#add = lambda x,y,z: x + y + z # This is anotther example of a lambda function
#full_name = lambda first_name, middle_name, last_name: first_name+" "+middle_name+" "+last_name # Lambda Function
age_check = lambda age: True if age >= 18 else False
#print(double(5))
#print(multiply(5,6))
#print(add(3, 6, 9))
#print(full_name("Brian", "Javelle", "Gates"))
print(age_check(18))