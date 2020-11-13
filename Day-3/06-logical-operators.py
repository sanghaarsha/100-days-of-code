# Logical Operators
# and
# or
# not

# Lets implement Logical Operators in the pizza order program
# Making Input Case Insensetive

print("Welcome to pizza order app.\n")

size = input("What size pizza do you want? (s,m,b) : ")
addPepperoni = input("Do you want to add pepperoni? (y/n) :")
addCheese = input("Do you want to add extra cheese? (y/n) :")

cost = 0

if (size == "s" or size == "S"): 
    cost += 15
    if(addPepperoni == "y" or addPepperoni == "Y"):
        cost += 2

if (size == "m" or size == "M"):
    cost += 20
    if(addPepperoni == "y" or addPepperoni == "Y"):
        cost += 3

if (size == "b" or size == "B"):
    cost += 25
    if(addPepperoni == "y" or addPepperoni == "Y"):
        cost += 3

if(addCheese == "y" or addCheese == "Y"):
    cost += 1

print(f"Your total cost is ${cost}.\n")
