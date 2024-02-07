# Dictionary - A changeable, unordered collection of unique key:value pairs. They are fast because use hashing,
#that allows us to access values quickly.
# Similar to a set, but instead we use key:value pairs.

capitals = {"USA": "Washington DC", "India": "New Dehli", "China": "Beijing", "Russia": "Moscow"}


print(capitals)
print(capitals.get("Germany")) # This allows us to check if a certain element is in our key:value pair.
print(capitals.keys()) # This function will return only the keys out of the key:value pairs.
print(capitals.values()) # This function allows us to return only the values of a key:value pair.
print(capitals.items()) # This function allows us to return each key:value pair separate
capitals.update({"Germany": "Berlin"}) # We can use this method to add a key:value pair to our dictionary
                                       # We can also use this method to change existing key:value pairs


for i in capitals:
    print(i) # This method will iterate only over the keys

capitals.pop("China") # This function removes a key:value pair

for key,value in capitals.items():
    print(key, value) # This method will iterate over each key:value pair



print(capitals)