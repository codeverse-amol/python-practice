# Local and Global Variables in Python
# Local Variables :
# Local variables are defined inside a function and can only be accessed within that function. They are created when the function is called and destroyed when the function exits.  
def my_function():
    local_variable = "I am a local variable"
    print(local_variable)

my_function()
# print(local_variable)  # This will raise an error because local_variable is not accessible outside


# Global Variables :
# Global variables are defined outside of any function and can be accessed from anywhere in the code, including inside functions. They are created when the program starts and destroyed when the program ends.
global_variable = "I am a global variable"  

def another_function():
    print(global_variable)  # This will work because global_variable is accessible inside functions

another_function()
print(global_variable)  # This will also work because global_variable is accessible outside functions

# Modifying Global Variables inside a Function :
# If you want to modify a global variable inside a function, you need to use the 'global' keyword to indicate that you are referring to the global variable, not creating a new local variable.
counter = 0  # This is a global variable    
def increment_counter():
    global counter  # This tells Python that we want to use the global variable 'counter'
    counter += 1  # This modifies the global variable
increment_counter()
print(counter)  # This will print 1, showing that the global variable was modified  






# Public, Private, and Protected Variables in Python :
# In Python, there are no strict access modifiers like in some other programming languages, but we can use naming conventions to indicate the intended level of access for variables.


# Public Variables : These are variables that can be accessed from anywhere in the code. They are defined without any special prefix.
public_variable = "I am a public variable"  


# Private Variables : These are variables that are intended to be accessed only within the class they are defined in. They are defined with a double underscore prefix (__).
class MyClass:
    def __init__(self):
        self.__private_variable = "I am a private variable"  # This variable is intended to be private
        print(id(self.__private_variable))  # Print the memory address of the private variable
    def access_private_variable(self):
        print(self.__private_variable)  # Accessing the private variable inside the class
        print(id(self.__private_variable))  # Print the memory address of the private variable
my_object = MyClass()
my_object.access_private_variable()  # This will work because we are accessing the private variable through
# a public method of the class
# print(my_object.__private_variable)  # This will raise an error because we cannot access the private variable directly from outside the class


# Protected Variables : These are variables that are intended to be accessed only within the class they are defined in and its subclasses. They are defined with a single underscore prefix (_).
class ParentClass:
    def __init__(self):
        self._protected_variable = "I am a protected variable"  # This variable is intended to be protected
class ChildClass(ParentClass):  
    def access_protected_variable(self):
        print(self._protected_variable)  # Accessing the protected variable in the child class 
child_object = ChildClass()
child_object.access_protected_variable()  # This will work because we are accessing the protected variable
# through a method of the child class
print(child_object._protected_variable)  # This will work, but it's not recommended to access protected variables directly from outside the class







class BankAccount:
    def __init__(self, owner, starting_balance):
        self.owner = owner
        self.__balance = starting_balance  # Private variable
        print(id(self.__balance))  

    # Public method to view the private variable
    def display_balance(self):
        # Accessing the private variable safely inside the class
        print(f"Account owner: {self.owner}")
        print(f"Current balance: ${self.__balance}")
        print(id(self.__balance)) 

    # Public method to modify the private variable
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # Modifying the private variable inside the class
        else:
            print("Invalid deposit amount!")

# --- Using the class ---
account = BankAccount("Alex", 1000)

# 1. This works perfectly because the function belongs to the class
account.display_balance()  

# 2. This updates it safely from the inside
# account.deposit(500)       
account.display_balance()
print(id(account._BankAccount__balance))  # Accessing the private variable using name mangling (not recommended)
# 3. This will crash! You cannot access it directly out here
# print(account.__balance)

