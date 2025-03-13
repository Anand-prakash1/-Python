'''Print Even and Odd Numbers

Write a program to iterate through numbers from 1 to 10.
Print "Even" if the number is even, else print "Odd".'''

# Loop through numbers from 0 to 9
for i in range(10):
    
    # Check if the number is even
    if i % 2 == 0:
        print(f"{i}: Even number")  # Print if even
    else:
        print(f"{i}: Odd number")   # Print if odd
