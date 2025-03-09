'''Write a Python program to check if one set is a subset of another.

 Input:
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

 Output:
A is a subset of B: True'''

# Taking input for the first set
# The input is split into individual elements, converted to integers, and stored in a set
set1 = set(map(int, input("Enter the elements of the first set: ").split()))

# Taking input for the second set and processing it in the same way as set1
set2 = set(map(int, input("Enter the elements of the second set: ").split()))

# Checking if set1 is a subset of set2
# A subset means all elements of set1 are present in set2
is_subset = set1.issubset(set2)

# Printing the result
print(f"set1 is a subset of set2: {is_subset}")
