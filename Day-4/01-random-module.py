# Importing the random module
import random

# 0 - 10
randInt = random.randint(0, 10)

print(randInt)

# 0 - 0.9999
randFloat = random.random()
print(randFloat)

# Random Float 0 - 10.9999
rand2 = (randFloat * 11)
print(rand2)
