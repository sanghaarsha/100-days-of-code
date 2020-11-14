import random
seedNum = int(input("Enter a random number: "))

nameAsCSV = input("Enter everybody's name separated by comma: ")
names = nameAsCSV.split(",")

length = len(names)-1
rand = random.randint(0, length)

print(names[rand])
