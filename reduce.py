# Reduce Function - Applies a function to an iterable and reduce it to a single cumulative value
# Performs function on first two elements and repeats process until 1 value remains

#reduce(function, iterable)

import functools

#letters = ["G", "A", "T", "E", "S"]
#word = functools.reduce(lambda x, y,: x + y,letters) # In this example, we reduced the length of the list to one item
#print(word)                                          #(GATES) by concatenating the first 2 items together, and then 
                                                      #repeating that process util one item remains. Example
                                                      #["G" + "A" = "GA" etc...]
                                                      #(lambda x, y,: x + y) is the function we used. (letters) is
                                                      #what was iterated through

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y,: x * y,factorial) # In this example, we use the same process as above, but this
print(result)                                            #time, we will be multipling the first 2 items before repeating
                                                         #the process with the rest of te items. Example
                                                         #[5 * 4 = 20 etc...]
                                                         #(lambda x, y,: x * y) is the function we used. (factorial) is
                                                         #what was iterated through