import time  # Import the time module

# Get the current hour as an integer (0-23)
timestamp = int(time.strftime('%H'))

# Print the type of the variable to confirm it's an integer
print(type(timestamp))

# Display the current hour
print("Time is :", timestamp)

# Determine the time of day and print an appropriate greeting
if 4 <= timestamp < 12:
    print("Good Morning")  # Morning: 4 AM - 11:59 AM
elif 12 <= timestamp < 15:
    print("Good Afternoon")  # Afternoon: 12 PM - 2:59 PM
elif 16 <= timestamp < 21:
    print("Good Evening")  # Evening: 4 PM - 8:59 PM
else:
    print("Good Night")  # Night: 9 PM - 3:59 AM
