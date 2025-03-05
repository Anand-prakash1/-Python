'''
Tuples are immutable, so we convert it into a list to modify elements.
append() adds "Russia" at the end.
insert() places elements at specific positions (e.g., "China" at index 0).
pop() removes elements by index before inserting new values.
Convert back to a tuple (tuple(temp)) after all modifications.
'''

# Define a tuple with country names
conteries = ("India", "Pakistan", "Bangladesh", "Afghanistan")

# Convert the tuple into a list to allow modifications
temp = list(conteries)

# Append "Russia" to the end of the list
temp.append("Russia")

# Insert "China" at the beginning of the list
temp.insert(0, "China")

# Remove the third element (originally "Bangladesh")
temp.pop(2)

# Insert "America" at the third position (index 2)
temp.insert(2, "America")

# Remove the fourth element (originally "Afghanistan")
temp.pop(3)

# Insert "Japan" at the fourth position (index 3)
temp.insert(3, "Japan")

# Remove the fifth element (originally "Russia")
temp.pop(4)

# Insert "New York" at the fifth position (index 4)
temp.insert(4, "New York")

# Convert the modified list back to a tuple
conteries2 = tuple(temp)

# Print the final modified tuple
print(conteries2)
