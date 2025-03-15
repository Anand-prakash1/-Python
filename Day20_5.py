# Taking user input as a string
a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")

try:
    # Looping from 1 to 10 to generate the multiplication table
    for i in range(1, 11):
        # Converting the input 'a' to an integer and printing the multiplication result
        print(f"{int(a)} X {i} = {int(a) * i}")  

# Handling exceptions in case the user enters a non-numeric value
except:
    print("Please enter a valid number")
