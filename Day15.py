# tuples......

# Define the first tuple with some integer values
tup1 = (1, 2, 34, 53, 53, 63)

# Define the second tuple with another set of integer values
tup2 = (10, 20, 30, 40, 50, 60)

# Concatenate both tuples to create a new tuple
tup3 = tup1 + tup2  

# Convert the tuple into a list, sort the elements, and convert it back to a tuple
tup3 = tuple(sorted(tup3))  

# Print the sorted tuple
print(tup3)
