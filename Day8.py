# Tuple is immutable
# changin tuple into list add element 10 
# then again change list into tupple 

tuple_1 = (1, 2, 3, 4, 5, 6, 7)
list_1 = list(tuple_1)
print("New list is: ")
list_1.append(10)
print(list_1)
print(type(list_1))
tuple_2 = tuple(list_1)
print(tuple_2)
print(type(tuple_2))
