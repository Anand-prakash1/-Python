'''
Write a Python program that takes two numbers 
as input and prints their division. If the denominator is 0, 
handle the error and print "Cannot divide by zero".
'''

# Taking input from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Using try-except to handle errors
try:
    # Attempting to convert inputs to integers and perform division
    print(f"{int(num1)} / {int(num2)} = {int(num1) / int(num2)}")

# Handling exceptions (catching any errors)
except:
    # Convert num2 to integer inside except block safely
    if int(num2) == 0:  # Checking if num2 is zero
        print("Can't divide by zero")
    else:
        print("Invalid input! Please enter numeric values.")
