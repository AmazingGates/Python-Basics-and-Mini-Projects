# Random Numbers - These are a few useful functions of Random Numbers
# In actualality, We will be going over Psuedo_Random Numbers. They aren't true random numbers, but they are close.
import random

x = random.randint(1,6) # This is an example of us getting back a random integer between 1 and 6
print(x)

y = random.random() # This is an example of getting back a random number between 0 and 1
print(y)

wives = ["Alia", "Brianna", "Mina", "Ayanna"]
z = random.choice(wives) # This is an example of us getting back a random choice from a list of values
print(z)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K"]
random.shuffle(cards) # This is an example of us shuffling randomly through a list of cards
print(cards)