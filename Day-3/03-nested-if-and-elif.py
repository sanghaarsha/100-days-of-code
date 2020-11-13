# multiple of if statements can be used inside if statements
# such used statements are called nested if statements

# lets do odd-even program using nested if:

num = int(input("Enter a number: "))

if(num >= 0):  # Checks if number is positive
    if(num % 2 == 0):  # nested if statement (if inside if)
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")
else:
    print("Please enter a positive number.")
