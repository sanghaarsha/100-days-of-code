print("Welcome to the tip calculator.\n")

total = float(input("What was the total bill? $"))
per = float(input("Enter tip percentage: "))

total += total * (per/100)

num = int(input("How many people are splitting the bill? "))

each = round(total/num, 2)

print(f"You have ${each} to pay.\n")
