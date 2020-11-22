import random

# Seeding is very important for generating almost true pseudo random numbers
testSeed = int(input("Enter a seed number: "))
random.seed(testSeed)

flip = random.randint(0, 1)

if flip == 1:
    print("Heads")
else:
    print("Tails")
