def factorial(n):
    if n == 0 or n == 1:  # Base case: Factorial of 0 or 1 is always 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call reducing n by 1 each time

# Take user input and convert it to an integer
n = int(input("Enter your number: "))

# Call the factorial function and print the result
print(f"Factorial of {n} is: {factorial(n)}")
