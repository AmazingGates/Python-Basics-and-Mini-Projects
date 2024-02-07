import time

time.sleep(2)
print("Good Morning, Welcome To Casa De Gates")
time.sleep(2)

name = input("Is This The Python Papi? ")
time.sleep(1)

if  name == "yes":
    print("Welcome Captain")
    time.sleep(2)
else:
    print("This Isn't for you!")

assist = ""
if name == ("yes"):
    assist = input("Would you like the secret message? ")
    time.sleep(2)
if assist == "yes":
    password = input("First, what is the password? ")
    time.sleep(1)
    if password == ("Gates Stay Gucci"):
        time.sleep(1)
        print("Indeed!")
        time.sleep(1)
        print("Message Incoming---")
        time.sleep(3)
        print("Message Incoming---")
        time.sleep(3)
        print("Message Incoming---")
        time.sleep(3)
        for i in range(0,21,1):
          if i == 1:
            print("They", end=" ")
          elif i == 2:
            print("Say", end=" ")
          elif i == 3:
            print("The", end=" ")
          elif i == 4:
            print("Game", end=" ")
          elif i == 5:
            print("Should", end=" ")
          elif i == 6:
            print("Be", end=" ")
          elif i == 7:
            print("Sold", end=" ")
          elif i == 8:
            print("Not", end=" ")
          elif i == 9:
            print("Told", end=" ")
          elif i == 10:
            print("But", end=" ")
          elif i == 11:
            print("That's", end=" ")
          elif i == 12:
            print("Hard", end=" ")
          elif i == 13:
            print("To", end=" ")
          elif i == 14:
            print("Control", end=" ")
          elif i == 15:
            print("When", end=" ")
          elif i == 16:
            print("Cats", end=" ")
          elif i == 17:
            print("Fold", end=" ")
          elif i == 18:
            print("Like", end=" ")
          elif i == 19:
            print("Paper Bags", end=", ")
          elif i == 20:
            print("And Rat!", end=" ")
          else:
            ""
    else:
        print("Nah Fam, F O H")
else:
    print("Safe Travels!")