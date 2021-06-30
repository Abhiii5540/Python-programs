# Create a list using []
a = [1, 2 , 4, 56, 6]

# Print the list using print() function
print(a)

# Access using index using a[0], a[1], a[2]
print(a[2])

# Change the value of list using
a[0] = 98
print(a)

# We can create a list with items of different types
c = [45, "Harry", False, 6.9]
print(c)

# List slicing
friends = ["Abhiii", "Tom", "Rohan", "Sam", "Divya", 45]
print(friends[0:4])
print(friends[-4:])

l1 = [1, 8, 7, 2, 21, 15]
print(l1)
l1.sort() # sorts the list
l1.reverse() # reverses the list
l1.append(45) # adds 45 at the end of the list 
l1.insert(2, 544) # inserts 544 at index 2
l1.pop(2) # removes element at index 2
l1.remove(21) # removes 21 from the list
print(l1)
