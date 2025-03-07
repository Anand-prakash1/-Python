# Function to compute the Fibonacci number at position 'n' using recursion
def fibonacci(n):
    # Check for invalid input (negative numbers)
    if n < 0:
        print("Invalid input")  # Fibonacci sequence is not defined for negative numbers
    # Base case: The first Fibonacci number (position 1) is 0
    elif n == 1:
        return 0
    # Base case: The second Fibonacci number (position 2) is 1
    elif n == 2:
        return 1
    # Recursive case: Sum of the two previous Fibonacci numbers
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)
            
# Taking user input for the Fibonacci position
n = int(input("Enter your number: "))

# Printing the Fibonacci number at position 'n'
print(fibonacci(n))
