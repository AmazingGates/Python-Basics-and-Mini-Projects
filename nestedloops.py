# Nested Loops - The "inner loop" will finish all of its iterations before finnishing one iteration from the 
#"outer loop"
rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") # We use the end="" method to keep our rows and colimns together, instead the code 
    print()                   #would return one character per row, per column. Try to remove it and run the code
                              #to see get an example of what that would like.
