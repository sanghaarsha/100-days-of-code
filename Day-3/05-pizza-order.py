print("Welcome to pizza order app.\n")

size = input("What size pizza do you want? (s,m,b) : ")
addPepperoni = input("Do you want to add pepperoni? (y/n) :")
addCheese = input("Do you want to add extra cheese? (y/n) :")

cost = 0

if (size == "s"):
    cost += 15
    if(addPepperoni == "y"):
        cost += 2

elif (size == "m"):
    cost += 20
    if(addPepperoni == "y"):
        cost += 3

elif (size == "b"):
    cost += 25
    if(addPepperoni == "y"):
        cost += 3

else:
    print("Invalid input!")

if(addCheese == "y"):
    cost += 1

print(f"Your total cost is ${cost}.\n")
