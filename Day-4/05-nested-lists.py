# Lists inside a list
# Here we have two lists inside a list dirty dozen
# First one is of fruits and second one is of veggies

dirtyDozen = [["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches",
               "Cherries", "Pears"], ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]]

# Printing out the list
print(dirtyDozen)

# Printing every items in the list
for a in dirtyDozen:
    print("\n")
    for item in a:
        print(item)
