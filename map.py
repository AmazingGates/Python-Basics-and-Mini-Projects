# Map - Applies a function to each item in an iterable(list, tuple, etc.)

#map(function, iterable) - The map() accepts 2 arguments, the () we want to use a (function), and an iterable (iterable)

# In this example we will be converting dollars to euros


store = [
    ("pants", 25.00),
    ("shirt", 20.00),
    ("jacket", 50.00),
    ("socks", 10.00)
]

to_euros = lambda data: (data[0], data[1]*0.82) # Lambda Function. We also used parentheses to allow "tuple" use
                                                # Also, only the data[1] will be multiplied by *0.82
to_dollars = lambda data: (data[0], data[1]/0.82) # This is how we convert to Dollars from euros

store_dollars = list(map(to_dollars, store))

#store_euros = map(to_euros, store) # In this example, (to_euros) is our function we will be passing as our first
                                   #argument. (store) is our iterable that we will be passing as our 2nd argument

store_euros = list(map(to_euros, store)) # This is the version we would use if we wanted to convert our map()
                                          #to an iterable. This will also return to us a new store with the new
                                          #converte prices

for i in store_euros:
    print(i)

for i in store_dollars:
    print(i)