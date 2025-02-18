# Taking user input for the number
num = int(input("Enter your number: "))

# Generating the multiplication table
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")  # Using f-string for cleaner formatting
