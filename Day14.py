# Lists are mutable in Python, meaning we can modify their elements after creation.

# Define a list with initial values
my_list = [1, 2, 3, 5, 6, 7]

# Print the type of the variable to confirm it's a list
print(type(my_list))  # Output: <class 'list'>

# Append an element (10) at the end of the list
my_list.append(10)  # List becomes [1, 2, 3, 5, 6, 7, 10]

# Insert an element (5) at index 0 (beginning of the list)
my_list.insert(0, 5)  # List becomes [5, 1, 2, 3, 5, 6, 7, 10]

# Print the final list after modifications
print(my_list)  # Output: [5, 1, 2, 3, 5, 6, 7, 10]
