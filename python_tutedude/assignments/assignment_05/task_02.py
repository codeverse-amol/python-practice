# Task 2: Demonstrate List Slicing 
# Problem Statement: Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list



# code:

# Original list
number_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list: {number_lst}")


extract = number_lst[:5]
print(f"Extracted first five elements: {extract}")


reverse = extract[::-1]
print(f"Reversed extracted elements: {reverse}")

#---End of code----