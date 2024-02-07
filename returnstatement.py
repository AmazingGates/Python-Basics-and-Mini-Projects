# Return Statement - Functions send Python values/objects back to the caller. These values/objects are known as
#the function's return value
def multiply(number_1,number_2):
    result = number_1 * number_2
    return result

print(multiply(9, 6))


# We can also simplify the return to use less space while coding. Same example as above, but simplified
def divide(number_1, number_2):
    return number_1 / number_2

print(divide(105,3))