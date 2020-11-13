name1 = input("Enter your name : ")
name2 = input("Enter His/Her name: ")

# Changing into lower-case and Concatening two names
name = name1.lower()+name2.lower()

# Counting true in Both names
trueCount = 0
trueCount += name.count("t")
trueCount += name.count("r")
trueCount += name.count("u")
trueCount += name.count("e")

# Counting love in Both names
loveCount = 0
loveCount += name.count("l")
loveCount += name.count("o")
loveCount += name.count("v")
loveCount += name.count("e")

# Calculating total
total = (trueCount*10)+loveCount

if(total <= 10):
    print(f"Your score is : {total}\nYou go together like coke and mentos.")
elif (total > 10 and total <= 50):
    print(f"Your score is : {total}\nYou are alright together.")
elif (total > 50 and total <= 80):
    print(f"Your score is : {total}\nYou are meant to be together.")
else:
    print(f"Your score is : {total}\nYour match was made in heaven.")
