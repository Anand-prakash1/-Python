# Loop through numbers from 0 to 14
for i in range(15):  
    # If i is 0, skip this iteration and move to the next number
    if i == 0:  
        continue  

    # If i is 5, skip this iteration and move to the next number
    if i == 5:  
        continue  

    # If i is 11, break out of the loop and stop execution
    if i == 11:
        break

    # Print the correct multiplication result
    print("5 x", i, "=", 5 * i)  
    
# Print a final message after the loop ends
print("Loop has finished executing.")
