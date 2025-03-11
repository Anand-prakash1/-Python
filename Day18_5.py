"""
Python Dictionary Operations
This script demonstrates basic dictionary operations such as adding, updating, deleting, and clearing elements.
"""

# Creating a dictionary with some initial key-value pairs
person = {"name": "Alice", "age": 25, "city": "Patna"}

# Displaying the original dictionary
print("Original Dictionary:", person)

# Updating a dictionary (Modifying existing values or adding new key-value pairs)
person.update({"name": "Anand" ,"age": 22, "job": "Software Engineer"})
print("After update:", person)

# Adding a new key-value pair
person["country"] = "India"
print("After adding a new key:", person)

# Removing an element using pop() (removes key and returns value)
removed_value = person.pop("city")  # Removes 'city' from dictionary
print(f"Removed 'city': {removed_value}")
print("After pop:", person)

# Removing an element using del (deletes key permanently)
del person["job"]
print("After del:", person)

# Clearing all elements from the dictionary
person.clear()
print("After clear:", person)  # Output: {}

# Checking if dictionary is empty
if not person:
    print("Dictionary is empty!")
