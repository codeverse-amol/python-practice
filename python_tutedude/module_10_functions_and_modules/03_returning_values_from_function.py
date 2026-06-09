# Returning Values from a Function in Python------------
# A function can send a value back to the place where it was called using the return statement.

# Why use return?
#--> To give back a result
#--> To use the output somewhere else
#--> To store the result in a variable


# Basic Example :
# def add(a, b):
#     return a + b

# result = add(5, 3)
# print(result)



# 1. Math functions (add, subtract, square, factorial, etc.)
# 2. String functions (count vowels, reverse string, check palindrome, etc.)
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in s:
        if ch in vowels:
            count += 1

    return count

vowel_count = count_vowels("Hello World")
print(f"Number of vowels in the string is: {vowel_count}")




def reverse_string(s):
    reversed_str = s[::-1]
    return reversed_str
reversed_s = reverse_string("Hello")
print(f"Reversed string is: {reversed_s}")




def is_palindrome(s):
    cleaned_str = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return cleaned_str == cleaned_str[::-1]

palindrome_check = is_palindrome("A man a plan a canal Panama")
print(f"Is the string a palindrome? {palindrome_check}")



# 3. List functions (max element, sum of list, filter even numbers, etc.)
# 4. Dictionary or set functions
# 5. User-input based functions

# --------------------------------------------------------------------------------------------------------------------------------- #

# 1. MATH FUNCTION PRACTICE
# Q1. Return cube of a number-
# Write a function that returns the cube of a number.

# def cube(n):
#     return n*n*n

# c = cube(2)
# print(f"Cube of given number is: {c}")


# Q2. Return the greatest of 3 numbers
# Write a function:
# def greatest(a, b, c):
# Return the largest number.

# def greatest(a, b, c):
#     return max(a, b, c)

# gr = greatest(3,10,400)
# print(f"Greatest number is: {gr}")


# Q3. Return True if number is prime

# Write a function that checks if a number is prime.
# using for loop-
# def prime(n):
    
#     if n < 2:
#         return False
    
#     for i in range(2, int(n**0.5)+1):

#         if n % i == 0:

#             return False
    
#     return True

# p = prime(11)
# print(p)

# using while loop-

# def prime(n):

#     if n < 2:
#         return False
    
#     i = 2
#     while i*i <= n:

#         if n % i == 0:
#             return False
#         i += 1

#     return True

# p = prime(5)
# print(p)

#--------------------------------------------------------------------------------------------------------------------------------------------------

# 2. STRING FUNCTION PRACTICE
# Q4. Count consonants
# Return number of consonants in a string.

# vowels = ["a", "e", "i", "o", "u"]

# def consonants(str):
#     count = 0

#     for ch in str.lower():  
#         if ch.isalpha() and ch not in vowels:
#             count += 1
#     return count

# s = consonants("python is programming language")
# print(s)



# Q5. Return string without spaces
# Input: "a m o l" → Output: "amol"

# def remove_space(str):

#     new_str = str.replace(" ","")
#     return new_str

# updated_str = remove_space("a m o l")
# print(updated_str)


# Q6. Return the word count in a sentence
# Input: "python is easy" → Output: 3

# def word_count(str):
#     c = str.split(" ")
#     return len(c)

# s = word_count("python is easy")
# print(s)

#---------------------------------------------------------------------------------------------------------------

# 📋 3. LIST FUNCTION PRACTICE
# Q7. Return squares of all numbers
# Input: [1,2,3] → Output: [1,4,9]


# s1 = []                     # create global variable so all appends will be get stored.

# def squares(n):
#     print(f"This program prints squares of given numbers\nInput => {n}")

#     for ch in n:
#         s = ch**2
#         s1.append(s)

#     return f"Output => {s1}"

# sq = squares([1,2,3])
# print(sq)



# Q8. Return only positive numbers
# Input: [-1,2,-3,4] → Output: [2,4]

# # code - 01 
# def positive_num(nums):
#     print("This program filters only positive numbers from the input.")
#     positive_numbers = [n for n in nums if n > 0]                           #- using list comprehension

#     return positive_numbers

# n = positive_num([-1,2,-3,4])
# print(n)




# # code - 02 - using lambda function
# def positive_num(nums):

#     print("This program filters only positive numbers from the input.")

#     p = list(filter( lambda x : x > 0, nums))


#     return p

# n = positive_num([-1,2,-3,4])
# print(n)



# Q9. Return second largest element
# Without using sort().

# def largest(nums):
#     largest = max(nums)             # 4
#     nums.remove(largest)

#     second_largest = max(nums)      # 2
#     return second_largest

# l = largest([-1,2,-3,4])
# print(l)

#----------------------------------------------------------------------------------------------------------------------------------------------------

# 🔢 4. SET FUNCTION PRACTICE
# Q10. Return union of 2 sets
# Q11. Return elements present in set A but not in set B
# Q12. Check if two sets are disjoint
# (If they have no common element → return True)

# 🗂️ 5. DICTIONARY FUNCTION PRACTICE
# Q13. Return dictionary keys sorted alphabetically
# Q14. Return students with marks > 50

# Input dictionary:

# {"amol": 40, "rohan": 77, "sita": 90}

# Q15. Create dictionary from 2 lists

# Input:
# names = ["a","b","c"]
# marks = [10,20,30]
# Output:
# {"a":10, "b":20, "c":30}

# 👨‍💻 6. USER-INPUT FUNCTION PRACTICE
# Q16. Take input name and age → return formatted string

# Output: "Your name is X and age is Y"

# Q17. Take list input from user → return its sum

# Example input:
# 1 2 3 4
# (convert into list inside function)

# Q18. Take 2 numbers from user → return their division