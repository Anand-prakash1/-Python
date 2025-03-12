# Question no.3
'''
Write a program to loop through a dictionary and 
print all keys and values.
'''

fruits = {"Apple": 100, "Banana": 50, "Mango": 80}
for key, value in fruits.items():
    print(key, value)
    
# Question no.4
'''
Write a program that checks if a given key exists in a dictionary.
'''

fruits = {"Apple": 100, "Banana": 50, "Mango": 80}
if "Apple" in fruits:
    print("Yes")
else:
    print("No")
