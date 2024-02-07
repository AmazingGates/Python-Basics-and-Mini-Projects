# Lists - These are a few useful functions of lists/[]

family = ["Brian", "Alia", "Bam Bam", "Ranya", "Mina"]

family.append("Baby Gates") # This function allows us to add items to our list.
family.remove("Ranya") # This function removes an item from the list
family.pop() # This function will remove the last item
family.insert(3, "Itachi") # This function allows us to insert an item at any location we choose
family.sort() # This function will sort a list alphabetacally
#family.clear() # This function will remove all the elements of a list/[]


for i in family:
    print(i)