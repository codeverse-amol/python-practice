# Level 3 – Hard
#============================================================================
# Problems =>
#============================================================================
# 1.Build a calculator using:
#   try
#   multiple except
#   else when valid operation
#   finally that prints “Calculation Done”

# 2.Write a function login(username, password) that:
#   Raises custom exception if username != "admin"
#   Raises custom exception if password length < 6
#   Wrap in try–except and print meaningful messages

# 3.Read all lines of a file.
#   If file not found → handle
#   If file is empty → raise your own exception

#============================================================================
# Answers =>
#============================================================================

# 1.Build a calculator using:
#   try
#   multiple except
#   else when valid operation
#   finally that prints “Calculation Done”


'''
# simple calculator:
print("\n#---Simple calculator---#\n")
def calculator():
    while True:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            operator = input("Enter operator: ")
            print("=====================")

            match operator:

                case "+":
                    print(f"Addition: {num1 + num2}")
                case "-":
                    print(f"Subtraction: {num1 - num2}")
                case "*":
                    print(f"Multiplication: {num1 * num2}")
                case "/":
                    print(f"Division: {num1 / num2}")
                case _:
                    print("Invalid Operator!!")
                    print("=====================")
                    break
                

        except ZeroDivisionError:
            print("Denominator should not be zero.")
            print("=====================")
            break
        except ValueError:
            print()
            print("Invalid Input!")
            print("=====================")
            break

        else:
            print("Calculation Done.")
            print("=====================")
            break

# calling function
calculator()

# keep asking user for operations until condition becomes false.
while True:
    more_cal = input("Do you want to do more calculations? (y/n): ").lower()
    print()
    if more_cal == "y":
        calculator()
        
    else:
        print("Quitting..")
        break

'''
#------------------------------------------------------------------------------
# 2.Write a function login(username, password) that:
#   Raises custom exception if username != "admin"
#   Raises custom exception if password length < 6
#   Wrap in try–except and print meaningful messages


'''
# Custom login function

print("\n#---Custom login function---#\n")

def login(username, password):
    try:
        # Check username
        if username != "admin":
            raise NameError("Incorrect username, Please enter a valid username.")

        # Check password length
        if len(password) < 6:
            raise ValueError("Password too short, Minimum length required is 6 characters.")

        print()
        print("Login successfully!!")
        return True
       

    except (NameError, ValueError) as e:
        print()
        print("Error:", e)
        print("Please try again...\n")


# Main Program
while True:
    try:
        user_name = input("Enter Username: ")
        pass_word = input("Enter Password: ")

        if login(user_name, pass_word):
            break
        

    except Exception as e:
        print("Error:", e)

'''
#------------------------------------------------------------------------------

# 3.Read all lines of a file.
#   If file not found → handle
#   If file is empty → raise your own exception
'''
try:
    with open("demo.txt", "r") as f:
        rf = f.read()
        print(rf)

        if len(rf)==0:
            raise ValueError("File is empty")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error: ", e)
'''