# Taking user input for a sentence
sentence = input("Enter Any sentence: ")

# Checking for spaces in the sentence
if "  " in sentence:  # Checking for double spaces first
    print("Your sentence contains double spaces")
elif " " in sentence:  # Checking for single spaces after
    print("Your sentence contains a single space")
else:  # If there are no spaces at all
    print("Your sentence contains no spaces")
