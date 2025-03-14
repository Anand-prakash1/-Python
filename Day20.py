# Taking user input
a = input("Enter the number: ")  

# Displaying the multiplication table header
print(f"Multiplication table of {a} is: ")

# Using try-except to handle invalid inputs
try:
    # Loop to generate multiplication table from 1 to 10
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a) * i}")  # Multiplication and display
except:
    # If the input is not a valid number, show an error message
    print("Please enter a valid number")  
