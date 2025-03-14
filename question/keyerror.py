'''
Create a dictionary of student names and their marks. 
Ask the user for a student’s name and print their marks. 
If the name is not found in the dictionary, print "Student not found".
'''

# Dictionary storing student names as keys and their respective marks as values
student_marks = {
    "Anand": 90,
    "Aman": 85,
    "Gaurav": 80,
    "Bittu": 75,
    "Yuvraj": 70
}

# Taking user input for the student's name
student = input("Enter the student's name: ")

try:
    # Fetch the student's marks safely
    print(f"{student}'s marks are: {student_marks[student]}")

# Exception handling (though not necessary in this case)
except:
    # This will print if an unexpected error occurs
    print("Student not found")
