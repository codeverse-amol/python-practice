# Task 2: Create a Personalized Greeting
# Problem Statement: Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.


# code:

# Taking first name and last name as input from the user
first_name = input("Enter user's first name: ")
last_name = input("Enter user's last name: ")
# Concatenating first name and last name to create full name
full_name = first_name +" "+ last_name
# Printing personalized greeting message
print(f"Hello, {full_name}! Welcome to the Python program.")