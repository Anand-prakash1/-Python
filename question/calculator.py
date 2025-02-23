# Taking user input for two numbers
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  

# Taking user input for an operator
operator = input("Enter an operator: /, *, +, -, **: ")  # Fixed spelling and added *

# Checking the operator and performing calculations
if operator == "/":  
    print("Result:", num1 / num2)  

elif operator == "*":  # Changed 'x' to '*', as 'x' is not a valid operator in Python
    print("Result:", num1 * num2)  

elif operator == "+":  
    print("Result:", num1 + num2)  

elif operator == "-":  
    print("Result:", num1 - num2)  

elif operator == "**":  # ** is exponentiation (power), not square root
    print("Result:", num1 ** num2)  

else:  
    print("Invalid operator! Please enter one of: /, *, +, -, **")
