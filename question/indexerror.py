'''
Write a program that asks the user for an index number and 
tries to access that index in a predefined list. 
Handle cases where the user enters an out-of-range index.
'''

# Creating a list with predefined elements
my_list = [10, 20, 30, 40, 50]

# Taking user input for index
index = input("Enter the index number: ")

# Using try-except to handle errors
try:
    # Converting input to integer and accessing the list element
    print(f"Element at index {index} is {my_list[int(index)]}")

# Handling possible errors
except IndexError:  
    # If the index is out of range, display an appropriate message
    print("Index out of range. Please enter a valid index.")
  
except ValueError:
    # If the user enters a non-numeric value, handle the error
    print("Invalid input! Please enter a number.")
