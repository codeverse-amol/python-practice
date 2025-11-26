# Task 1: Create a Dictionary of Student Marks

# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.



# code:

# Dictionary with students name and marks
student = {'Alice': 85, 'Harsh': 90, 'Sam': 75, 'Jack': 95}

# taking input from user
key = input("Enter the student's name: ")

# Checking if the name exists in dictionary
if key in student:
    print(f"{key}'s marks: {student[key]}")
else:
    print("Student not found.")

#---End of code----