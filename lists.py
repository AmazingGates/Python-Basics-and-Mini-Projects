# Lists - Used to store multiple items in a single variable
food = ["pizza", "hamburger", "steak", "crinkley fries"]

food[0] = "chicken tenders" # We use this method to change items in our list without having to go into the actual list

print(food)
print(food[2]) # We can single out items by indexing into the food list/[], by using the with the items location ([2])

for x in food:
    print(x, end=", ")