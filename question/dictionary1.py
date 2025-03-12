# Question no.1
'''
Create a dictionary of country codes (e.g., 
{"IN": "India", "US": "United States"}).
Use the get() method to retrieve the country name for a given code.
'''

country_code = {"In":"India", "US":"United States"}
print(country_code.get("US"))

# Question no.2
'''
Create a dictionary of fruits with their prices.
Update the price of a fruit and add a new fruit.
'''

fruits = {"Apple": 100, "Banana": 50, "Mango": 80}
fruits["Banana"] = 80
fruits["Apple"] = 120
fruits["Mango"] = 110
fruits.update({"Gwava": 60})
print(fruits)
