''' 
Dictionary.............
- A dictionary is a collection of key-value pairs.
- Dictionaries are unordered, changeable (mutable), and indexed.
'''

# Creating a dictionary with key-value pairs
dic = {"name": "Anand", "age": 22, "job": "Web Developer"}

# Accessing values using square brackets []
print(dic["name"])  # Output: Anand

# Accessing values using get() method (prevents errors if the key doesn't exist)
print(dic.get("age"))  # Output: 22
print(dic.get("job"))  # Output: Web Developer

# Looping through dictionary items (key-value pairs)
for key, value in dic.items():
    print(f"{key}: {value}")  
