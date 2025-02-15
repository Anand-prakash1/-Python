
a = "@@@@@@String@@@@@@@@"
print(a.upper()) #Strings are immutable we cant 
                 #change it but we create another
print(a.lower())
print(a.rstrip("@")) #cant change starting strip
b = a.replace(a , "anand") #replace a variable to Anand
print(b) 
print(b.capitalize()) #capitalize first letter
print(b.count("n")) #count the number of n in string
print(a.find("a")) #there in no a letter n a variable 
print(b.find("n")) #index of n
