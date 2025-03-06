# Define a string with placeholders `{}` for inserting values dynamically
letter = "Hey my name is {} and I am from {}"

# Define values for the placeholders
name = "Anand"
country = "India"

# Use the format() method to replace `{}` with actual values (name and country)
formatted_letter = letter.format(name, country)

# Print the formatted string
print(formatted_letter)
