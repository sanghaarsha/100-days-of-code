# TypeErrors are raised when the programmer fails to check the type of object before performing an operation on them.

# For example adding a integer to the string
# print(22+"hello")

# To avoid we must check passed object are of same types
# Python provides built in function to check types
# type(data)

# Type is shown like this : <class 'type'>

print(type(22))  # <class 'int'>
# int : means its an integer

print(type("Hello"))  # <class 'str'>
# str : means its an string


# Lets do type conversion
a = "123"  # string type
b = 123.45  # float type

# if we add them without conversion we will get an error
# so lets convert a into float
a = float(a)
print(a+b)  # 246.45
# numbers get added and printed in the terminal
