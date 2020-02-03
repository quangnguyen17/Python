
import random


def randInt(min=0, max=100):
    return random.random() * (max - min) + min


print(randInt()) 		    # should print a random integer between 0 to 100
print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print(randInt(min=50)) 	    # should print a random integer between 50 to 100
# should print a random integer between 50 and 500
print(randInt(min=50, max=500))
