# Take space-separated integer input from the user and convert it into a list
list1 = list(map(int, input("Enter elements: ").split()))

# Remove duplicates by converting the list into a dictionary (keys remain unique), then convert back to a list
list2 = list(dict.fromkeys(list1))

# Reverse the list in place
list2.reverse()

# Print the reversed list without duplicates
print(list2)
