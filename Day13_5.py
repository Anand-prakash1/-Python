# Write a user-defined function in Python called find_average() that takes a list of numbers as an argument and returns the average (mean) of those numbers.

import statistics  # Importing the statistics module to use built-in functions

# Function to calculate the average (mean) of a list of numbers
def Find_Average(data):
    Average = statistics.mean(data)  # Calculate the mean using statistics.mean()
    print("Average:", Average)  # Print the calculated average

# Taking user input as a space-separated list of numbers
data = list(map(int, input("Enter numbers separated by space: ").split()))

# Calling the function with the user-provided data
Find_Average(data)

