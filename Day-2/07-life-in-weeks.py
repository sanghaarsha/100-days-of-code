print("Assuming we live up to 90 Years,\nThis program calculates your time left on Earth.\n")

age = int(input("Enter your age: "))

days = (90 - age)*365
weeks = int(days/7)
months = int(days/30)

print(f"You have {days} days,{weeks} weeks,{months} months left.\n")
