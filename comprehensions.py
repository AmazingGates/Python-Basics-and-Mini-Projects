# List Comprehensions - A way to create a new list with less syntax
# Can mimic certain lambda functions, easier to read

#list = [expression for item in iterable]
#list = [expression for item in iterable if conditional]
#list = [expression if/else for item in iterable]

print("--------------------------------------------------------------")
print("--------------------------------------------------------------")

students = [100,90,80,70,60,50,40,30,0] # In this example, we used filter() to mimic some of the 
                                         #lambda functions features
#passed_students = list(filter(lambda x: x >= 60, students))

#passed_students = [i for i in students if i >= 60]

passed_students = [i if i >= 60 else "FAILED" for i in students] # Here, we iterated through our students list
                                                                  #and returned all the passing grades 60 or above
                                                                  #as integers, but replaced all the failing grades
                                                                  #with the word/string "Failed".

print('Here, we iterated through our students list and returned all the passing grades 60 or above\
 as integers, but replaced all the failing grades with the word/string "Failed".')

print("--------------------------------------------------------------")

print("students = [100,90,80,70,60,50,40,30,0]")

print("--------------------------------------------------------------")
print("--------------------------------------------------------------")

print(passed_students)

print("--------------------------------------------------------------")
print("--------------------------------------------------------------")


print("In the example below we are just using this program to serve as a refrence point for a good place to use\
 a list comprehension. When we run the program we return a list of numbers from 1 to 10, with each number in sequence\
being represented by it's squared value.")

print("--------------------------------------------------------------")
print("--------------------------------------------------------------")

squares = []
for i in range(1,11):
    squares.append(i * i)
print(squares)

print("--------------------------------------------------------------")
print("--------------------------------------------------------------")

print(" The example below is a representation of the code above. The only difference is this time we will be using\
 a list comprehension to build our code. This helps us use less syntax and makes our code easier to read.")

print("--------------------------------------------------------------")
print("--------------------------------------------------------------")

squares = [i * i for i in range(1,11)]
print(squares)

print("--------------------------------------------------------------")
print("--------------------------------------------------------------")