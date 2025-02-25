# Function to calculate the geometric mean
def CalculateGmean(a, b):
    # Formula for geometric mean
    mean = (a * b) / (a + b)
    print(mean)

# Taking input from the user for the first pair of numbers
a = int(input("Enter your first number: "))  # First number
b = int(input("Enter your second number: "))  # Second number

# Calling the function with the first pair of numbers
CalculateGmean(a, b)

# Taking input from the user for the second pair of numbers
c = int(input("Enter your first number: "))  # Third number
d = int(input("Enter your second number: "))  # Fourth number

# Calling the function with the second pair of numbers
CalculateGmean(c, d)

