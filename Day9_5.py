# Asking the user to input a number between 1 and 7
Day = int(input("Enter a number between 1 to 7: "))

# Using the match-case statement (Python 3.10+ feature) to check the input
match Day:
    case 1:
        print("Sunday")  # If the user enters 1, print "Sunday"
    case 2:
        print("Monday")  # If the user enters 2, print "Monday"
    case 3:
        print("Tuesday")  # If the user enters 3, print "Tuesday"
    case 4:  
        print("Wednesday")  # If the user enters 4, print "Wednesday"
    case 5:
        print("Thursday")  # If the user enters 5, print "Thursday"
    case 6:
        print("Friday")  # If the user enters 6, print "Friday"
    case 7:
        print("Saturday")  # If the user enters 7, print "Saturday"
    case _:
        print("Invalid input! Please enter a number between 1 and 7.")  
        # If the user enters anything other than 1-7, print an error message
