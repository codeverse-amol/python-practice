# ✅ 1. PRACTICE QUESTIONS — CONSTRUCTOR (__init__)

# Q1. Create a class Book with title, author, and price.
# Use a constructor to initialize them and create 3 objects.

# Q2. Create a class Employee with a constructor that auto-generates employee IDs
# like: E101, E102, E103 (Hint: use a class variable).

# Q3. Write a class BankAccount with:
# constructor to set name and balance
# method display()
# Create 2 accounts and display their details.

# Q4. Create a class Student with:
# name

# 5 subject marks
# Write a method to calculate total and average.

# Q5. Make a class Rectangle with length and width from constructor
# Find area and perimeter.







#-----------------------------------------------------------------------------------------------------------------------------
# Q1. Create a class Book with title, author, and price.
# Use a constructor to initialize them and create 3 objects.

# ans: 

# class Book:

#     def __init__(self, title, author, price):

#         self.title = title
#         self.author = author
#         self.price = price


#     def show_book(self):
#         print(f"The author of '{self.title}' is '{self.author}'.")


# b1 = Book("You Got This", "Gianna Mago", 295)
# b1.show_book()
#-----------------------------------------------------------------------------------------------------------------------------
# Q2. Create a class Employee with a constructor that auto-generates employee IDs like: E101, E102, E103 (Hint: use a class variable).

# ans: 

# class Employee:

#     emp_count = 100  # class variable to track last used ID

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#         # Auto-generate employee ID
#         Employee.emp_count +=1
#         self.emp_id = f"E{Employee.emp_count}"


#     def show_details(self):

#         print(f"Employee Id: {self.emp_id}")
#         print(f"Name: {self.name}")
#         print(f"Salary: {self.salary}")
#         print("-"*30)
        
# # ---------------------------
# # Creating employee objects
# # ---------------------------
# e1 = Employee("John",45000)
# e2 = Employee("Alice",60000)
# e3 = Employee("Jerry",50000)

# # Show details
# e1.show_details()
# e2.show_details()
# e3.show_details()

#-----------------------------------------------------------------------------------------------------------------------------
# Q3. Write a class BankAccount with:
# constructor to set name and balance
# method display()
# Create 2 accounts and display their details.

# ans: 


# class BankAccount:

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

    
#     def display(self):
#         print(f"Acc Name: {self.name}")
#         print(f"Acc Balance: {self.balance}")
#         print("-"*20)

# b_a1 = BankAccount("John", 200000)
# b_a2 = BankAccount("Alice", 500000)
# b_a1.display()
# b_a2.display()
#-----------------------------------------------------------------------------------------------------------------------------

# Q4. Create a class Student with:
# name

# ans: 

# class Student:

#     def __init__(self, name):
#         self.name = name

#     def student_info(self):
#         return f"Student name is {self.name}"


# s1 = Student("Andrew")
# s2 = Student("Maddy")

# print(s1.student_info())
# print(s2.student_info())

#-----------------------------------------------------------------------------------------------------------------------------

# Q5. Make a class Rectangle with length and width from constructor
# Find area and perimeter.

# ans: 

# class Rectangle:

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
        
#     # area of a rectangle is : A = L × W
#     def area(self):
#         print(f"area of rectangle is: ", self.length * self.width)

#     # perimeter of a rectangle is : P = 2(l + w)
#     def perimeter(self):
#         print(f"perimeter of rectangle is:", 2*(self.length + self.width))


# r1 = Rectangle(20, 25)
# r1.area()
# r1.perimeter()

