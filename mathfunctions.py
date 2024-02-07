# Math Functions - These are a few useful functions related to numbers in Python
import math

pi = 3.14
x =1
y = 2
z = 3

print(round(pi)) # In this example we used the round() to round our float to its nearest integer.
print(math.ceil(pi)) # This allows us to round up to the nearest whole integer
print(math.floor(pi)) # This allows us to round down to the nearest whole integer 
print(abs(pi)) # This will give us the absolute value of a number
print(pow(pi, 3)) # This allows us to raise a base number by a power. To do this we pass in two arguments, a 
#base(pi) and an exponent(3)
print(math.sqrt(pi)) # This allows us to get the square root of a nunber
print(max(pi, x, y, z)) # This allows us to the find maximum value between variables
print(min(pi, x, y, z)) # This allows us to find the minimum value between variables