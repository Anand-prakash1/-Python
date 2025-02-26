
import statistics  # Importing the statistics module (not needed for range calculation)

# Function to calculate the range
def Range(data):
    range_value = max(data) - min(data)  # Calculate the range (max - min)
    print("Range:", range_value)  # Print the calculated range

# Taking user input as a space-separated list of numbers
data = list(map(int, input("Enter numbers separated by space: ").split()))

# Calling the function with the user-provided data
Range(data)
