# Loop through numbers from 0 to 14
for i in range(15):  
    # Print the multiplication result (incorrect calculation due to +1)
    print("5 x", i, "=", 5 * i + 1)  
    
    # Stop the loop when i reaches 10
    if i == 10:  
        break  
    print("Loop end")
