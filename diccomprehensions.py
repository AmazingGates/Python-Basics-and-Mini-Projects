# Dictionary Comprehensions - Creates Dictionarie using an expression. Can replace for loops 
#and certain lambda functions

# dictionary = {key: expression for (key,value) in iteration} # This is the formula to use a Dictionary Comprehension

# dictionary = {key: expression for (key,value) in iteration in iterable if contional} # This is the formula 
#to add an if statement to our Dictionary Comprehension

# dictionary = {key: if/else for (key,value) in iterable} # This is the formula to add an if/else to our
#Dictionary Comprehension

# dictionary = {key: function(value) for (key,value) in iterable} # This the formula to add a function to our
#Dictionary Comprehension







# In the example below, we will take cities_in_F (short to fharanheight), and convert them to 
#cities_in_C (short for celcius) using a Dictionary Comprehension

cities_in_F = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}

cities_in_C = {key: round((value-32)* (5/9)) for (key,value) in cities_in_F.items()} # We also added a round() to
print(cities_in_C)                                                                   #make the returns more readable


# In the example below we will be iterating through the weather dict/[], and only returning keys with a "sunny" value
# We then stored those items in a new dict/[], (sunny_weather) so that we may print the returned items
# To acheive this, we iterated through our Dictionary Comprehension with an if statement
weather = {"New York": "snowing", "Boston": "sunny", "Los Angeles": "sunny", "Chicago": "cloudy"}

sunny_weather = {key: value for key,value in weather.items() if value == "sunny"} # This is the formula we used
print(sunny_weather)                                                              #to add an if statement to our
                                                                                  #Dictionary Comprehension


# In the example below we will be using an if/else in our Dictionary Comprehension to replace to the
#weather temperaturewith a description of the weather
cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}

desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
print(desc_cities)


# In the example below we will be adding a function to our Dictionary Comprehension to do the same thing as 
#the code above, but instead of using a if/else, we will be using a function

def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities_1 = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}

desc_cities_1 = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities_1)