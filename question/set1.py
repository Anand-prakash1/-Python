'''Write a program to find the difference and 
 symmetric difference between two sets.
 
input:
 X = {5, 10, 15, 20}
Y = {10, 20, 30, 40}

output:
Difference (X - Y): {5, 15}
Symmetric Difference: {5, 15, 30, 40}
 '''
 
# Solution:
# Taking input for the first set, splitting it into individual elements,
# converting them to integers, and storing them in a set.
set1 = set(map(int, input("Enter the elements of the first set: ").split()))

# Taking input for the second set and processing it in the same way as set1.
set2 = set(map(int, input("Enter the elements of the second set: ").split()))

# Finding the difference between set1 and set2.
# Difference (A - B) returns elements that are in set1 but NOT in set2.
difference = set1.difference(set2)

# Finding the symmetric difference between set1 and set2.
# Symmetric difference (A △ B) returns elements that are in either set1 or set2, but NOT in both.
symmetric_difference = set1.symmetric_difference(set2)

# Printing the results
print(f"Difference (set1 - set2): {difference}")
print(f"Symmetric Difference: {symmetric_difference}")
