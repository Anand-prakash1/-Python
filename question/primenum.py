def isprime(data):
    """
    Function to check if a number is prime.
    A prime number has exactly two divisors: 1 and itself.
    """
    count = 0  # Counter to count the number of divisors
    i = 1  # Start checking divisibility from 1

    while i <= data:  # Loop from 1 to the given number
        if data % i == 0:  # Check if 'data' is divisible by 'i'
            count = count + 1  # Increase the count if it is a divisor
        i = i + 1  # Increment loop variable

    # A prime number has exactly two divisors: 1 and itself
    if count == 2:
        print("Prime number")  # If count is 2, it's a prime number
    else:
        print("Number isn't prime")  # Otherwise, it's not a prime number

# Take input from the user
data = int(input("Enter a number: "))  # Prompt user for input and convert to integer

# Call the function to check if the number is prime
isprime(data)
