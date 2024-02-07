# Filter Function - Creates a collection of elements from an iterable for which function returns True

# filter(function, iterable)

family = [
    ("Alia", 35),
    ("Brian", 42),
    ("Bam Bam", 3),
    ("Amelia", 1)
]

# In the code below, we are filtering through the tuples and returning everyone equal to or older than 18, and creating
#a new list with the returned results and storing them in a variable called (mother_father)
age = lambda data:data[1] >= 18 # Lambda Function

mother_father = list(filter(age, family))

for i in mother_father: # We then iterate through that newly formed list in our mother_father variable and print
    print(i)            #the items within