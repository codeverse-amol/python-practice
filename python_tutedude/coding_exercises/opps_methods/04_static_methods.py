# ✅ 4. PRACTICE QUESTIONS — STATIC METHODS (@staticmethod)
# Q1. Create a class MathUtil with static methods:
# is_even(n)
# is_prime(n)
# square(n)
# Call these without making an object.

# Q2. Create class Validator with static method:
# validate_email(email) → return True/False using regex.

# Q3. Create class PasswordChecker with static method:
# check length ≥ 8
# has digit
# has uppercase
# has special char

# Q4. Create class TimeHelper with static method:
# convert seconds → hours, minutes, seconds tuple

# Q5. Create class StringTools with static method:
# count_vowels(string)
# is_palindrome(string)
#----------------------------------------------------------------------------------
# Q1. Create a class MathUtil with static methods:
# is_even(n)
# is_prime(n)   
# square(n)
# Call these without making an object.

# Solution:

class MathUtil():

    @staticmethod
    def is_even(n):
        if n % 2 == 0:
            print("Even number")
        else:
            print("Odd number")

    @staticmethod
    def is_prime(n):
        if n < 2:
            print("Not Prime")
        else:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    print("Not Prime")
                    break
            else:
                print("Prime")
        
    @staticmethod
    def square(n):
        s = n * n
        print(s)


MathUtil.is_even(2)
MathUtil.is_prime(97)
MathUtil.square(8)

#----------------------------------------------------------------------------------
# Q2. Create class Validator with static method:
# validate_email(email) → return True/False using regex.


# Solution:

import re

class Validator:

    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return True
        return False


# Testing
print(Validator.validate_email("test@example.com"))   # True
print(Validator.validate_email("invalid-email@"))      # False

#----------------------------------------------------------------------------------
# Q3. Create a class PasswordChecker that contains a static method named check_password(password).

# The method should return True if the password meets all these conditions:
# Length is at least 8 characters
# Contains at least one digit (0–9)
# Contains at least one uppercase letter (A–Z)
# Contains at least one special character
# (examples: ! @ # $ % ^ & * ( ) _ + - = etc.)
# If any condition is missing, return False.


# Solution:

class PasswordChecker:

    @staticmethod
    def check_password(password):
        # Condition 1: length >= 8
        if len(password) < 8:
            return False

        # Condition 2: has at least one digit
        has_digit = any(char.isdigit() for char in password)

        # Condition 3: has uppercase letter
        has_upper = any(char.isupper() for char in password)

        # Condition 4: has special character
        special_chars = "!@#$%^&*()-_=+[]{};:',.<>?/|`~"
        has_special = any(char in special_chars for char in password)

        return has_digit and has_upper and has_special


# Testing
print(PasswordChecker.check_password("Hello123!"))   # True
print(PasswordChecker.check_password("hello123"))    # False (no uppercase, no special)
print(PasswordChecker.check_password("HELLO!!!"))    # False (no digit)

PasswordChecker.check_password("Abcd@1000")
#------------------------------------------------------------------------
# Q4. Create class TimeHelper with static method:
# convert seconds → hours, minutes, seconds tuple

class TimeHelper:
    @staticmethod
    def convert(seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        sec = seconds % 60
        return hours, minutes, sec


# Example
print(TimeHelper.convert(3665))   # Output → (1, 1, 5)



#------------------------------------------------------------------------
# Q5. Create class StringTools with static method:
# count_vowels(string)
# is_palindrome(string)

class StringTools:
    @staticmethod
    def count_vowels(string):
        vowels = "aeiouAEIOU"
        return sum(1 for char in string if char in vowels)

    @staticmethod
    def is_palindrome(string):
        cleaned = string.replace(" ", "").lower()
        return cleaned == cleaned[::-1]


# Examples
print(StringTools.count_vowels("Amol Bandgar"))   # → vowel count
print(StringTools.is_palindrome("madam"))         # → True
print(StringTools.is_palindrome("hello"))         # → False
