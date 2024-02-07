# Nested Function Calls - Function calls inside of other functioncalls. Innermost functions are resovled first
# Returned value is used as parameter for the next outer function.
# In the example below we go through the steps of using a nested function. This function will work its way from the
#inside out. Meaning the innermost functions will be run first when the function is called, and the outer 
#functions will follow
print(round(abs(float(input("Enter a whole positive number: "))))) # In this example we used the input(), inside 
#the float(), inside the absolute abs(), inside the round(), all wrapped inside print().