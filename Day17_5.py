
# Creating the first set with numbers from 1 to 10
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Creating the second set with overlapping and additional numbers
set2 = {10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 15, 16, 17, 18, 19, 20}

# Finding the union of both sets (all unique elements from both sets)
uni = set1.union(set2)
print("Union of set1 and set2:", uni)

# Finding the intersection of both sets (common elements in both sets)
inter = set1.intersection(set2)
print("Intersection of set1 and set2:", inter)  # Output: {1, 2, 3, 4, 5, 10}

# Finding the difference (elements in set1 but not in set2)
diff = set1.difference(set2)  
print("Difference (set1 - set2):", diff)  # Output: {6, 7, 8, 9}

# Alternative: Difference in the other direction (set2 - set1)
diff2 = set2.difference(set1)
print("Difference (set2 - set1):", diff2)  # Output: {11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
