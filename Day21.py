# finally keyword

# Taking user input, splitting it into individual values, converting them into integers, and storing them in a list
list = list(map(int, input("Enter two numbers: ").split()))

try:
    # Calculating the difference between the maximum and minimum values in the list
    print(max(list) - min(list))

# Handling any errors that may occur, such as non-numeric input
except:
    print("Invalid input! Please enter numeric values.")

# The 'finally' block executes regardless of whether an exception occurs or not
finally:
    print("Always executed!")
