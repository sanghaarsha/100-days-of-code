# Lets write a program that switches values of variables

a = int(input("a: "))
b = int(input("b: "))

print("\nBefore Switching:")
print("a b")
print(a, b)

# switching values
c = a
a = b
b = c

print("\nAfter Switching:")
print("a b")
print(a, b)
