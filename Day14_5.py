
''' Write a Python function that takes a list as input 
and returns a new list with duplicates removed, maintaining the 
original order.'''

# Define a list with duplicate elements
list1 = list(map(int, input("Enter numbers separated by space: ").split()))

# Using dict.fromkeys() to remove duplicates while maintaining order
uniq_list = list(dict.fromkeys(list1))

# Print the unique list
print(uniq_list)  # Output
