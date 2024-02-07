# Loop Control Statements - Used to change a loops execution from its normal sequence

# break - Used to termiinate the loop entirely
# continue - Skips to the next iteration of the loop
# pass - Does nothing. Acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break


phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="") # We used the end="" method to return all of values back on the same line as opposed to stacked


for i in range(1,21):

    if i == 13:
        pass
    else:
        print(i, end="")