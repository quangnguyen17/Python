
# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello ", name)    # with a comma
print("Hello " + name)    # with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello ", name, "!")    # with a comma
print("Hello ", name, "!")    # with a +    -- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
food_one = "sushi"
food_two = "pizza"
print("I love to eat {} and {}".format(food_one, food_two)) # with .format()
print(f"I love to eat {food_one} and {food_two}.") # with an f string

def sum(num1, num2):
    return num1 + num2
