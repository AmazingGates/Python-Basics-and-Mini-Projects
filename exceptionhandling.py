# Execption Handling - Events detected during execution that interrupt the flow of a program
try: # This feature allows us to catch possible errors in our code
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except Exception as e: # This feature allows us to print a warning message if we do encounter an error
    print(e)
    print("SOMETHING WENT WRONG!!!")
except ZeroDivisionError as e: # By adding the "as e" to the end of this line we can 
    print(e)                          #pass and print the actual error code
    print("YOU CAN'T DIVIDE BY 0")
except ValueError as e:
    print(e)
    print("NOT A VALID NUMBER")
else:
    print(result)
finally: # This alllows us to execute the finally block weather we catch n error or not
    print("This Will Always Print")