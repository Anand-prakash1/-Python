import statistics

# Define the function with a parameter
def CalculateMedian(data):
    median = statistics.median(data)  # Compute median
    print("Median:", median)  # Print result

# Take input as a list of numbers
data = list(map(int, input("Enter numbers separated by space: ").split()))

# Call the function with the data
CalculateMedian(data)
