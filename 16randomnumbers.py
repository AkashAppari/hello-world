#Random Numbers in Python

#importing "random" for random operations
import random

#using choice() to generate a random number from a given list of numbers
print("A random number from list is :",end="")
print(random.choice([1,4,8,10,30]))

#using randrange() to generate in range from 20 to 50. The last parameter 3 is step size to skip three numbers while selecting
print("A random number from range is: ",end="")
print(random.randrange(20,50,3))