# Taking user input for weather condition
weather = input("Enter weather info: ")  

# Checking the weather condition using if-elif-else statements
if weather == "sunny":
    # If the weather is sunny, print this message
    print("Today's weather is too good, go to school")  

elif weather == "cloudy":
    # If the weather is cloudy, print this message
    print("Weather is ok, you can go to school")  

elif weather == "rainy":
    # If the weather is rainy, print this message (reminder to take an umbrella)
    print("Today's a rainy day, don't forget an umbrella when going to school")  

elif weather == "windy":
    # If the weather is windy, print this caution message
    print("Weather is too windy, be careful if you go to school")  

else:
    # If the user enters an invalid weather type, print an error message
    print("Invalid weather. Please enter sunny, cloudy, rainy, or windy")  
