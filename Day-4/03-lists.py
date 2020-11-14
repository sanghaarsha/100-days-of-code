# Creating lists
# Store related data
# Data are stored in order

districts = ["Chitwan", "Kathmandu", "Lamjung", "Baglung"]

# Acessing by index
print(districts[0]) # first index : 0
print(districts[1])

# Altering items in a list
districts[0] = "Solukhumbu"

# Adding item to a list
districts.append("Jumla")

# extending a list
districts.extend(["Chitwan","Humla"])

# Displaying all items
for item in districts:
    print(item)
