# Primitive Data Types :
# 1. String
# 2. Integer
# 3. Float
# 4. Boolean

# String :
# Its just String of characters, eg. "Hello", "John Doe"
# It will show character at index 0 (index 0 = first element)
# This is called subscripting
a = "Hello"
# type() displays type of provided argument
print(type(a))  # <class 'str'>
print(a[0])  # H

# Remember whatever data you keep inside double qoutes is string
# It will join these strings not add them as you expect because they are strings
print("123"+"456")  # 123456


# Integer :
# All whole numbers without decimal places (both positive and negative)
b = 123
print(type(b))  # <class 'int'>
print(b)  # 123
print(123+456)  # 579
# They are added not joined

# The underscores are ignored in a integer by the compiler
# Underscores can be used as commas, but compiler will ignore it
c = 123_456_789
print(c)  # 12345679

# Float
# Numbers with decimal places
d = 1.2345  # <class 'float'>
print(type(d))
print(d)  # 1.2345

# Boolean
# True or False
# Must Begin With Capital Letter
e = True
print(type(e))
print(e)
