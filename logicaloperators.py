# Logical Opertaors (and, or, not) - These are used to check if two or more conditional statements are true
# With the Logical Operator (and), both conditions MUST be true before the statement is considered true.
# With the Logical Operator (or), only one of the conditions have to be true for the whole statement to be 
#considered true
# With the Logical Operator (not), it takes a statement and wraps in parentheses and automatically makes 
#the statement opposite of itself. example (not(makes sense)) means that if the value makes sense
#it's false, and if it doesn't make sense, it's true.
temp = int(input("What's the weather like? "))

if temp >= 65 and temp <= 85:
    print("It's nice outside today!")
    print("Let's go be famous...")

elif temp < 65 or temp > 95:
    print("Nah, I'll probably be inside today.")
    print("Come and check me tomorrow.")