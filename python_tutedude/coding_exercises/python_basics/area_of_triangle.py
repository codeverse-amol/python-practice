# This program calculates the area of a triangle using Heron's formula.

'''
side_1 = int(input("Enter length of side 1: "))
side_2 = int(input("Enter length of side 2: "))
side_3 = int(input("Enter length of side 3: "))

p = (side_1 + side_2 + side_3)/2

area =(p*(p-side_1)*(p-side_2)*(p-side_3))**0.5

print("The area of the traingle is :", round(area, 2))      #rounded to 2 decimal places(float value)
'''

# calculate area of triangle using height and base i.e right angle triangle
'''
base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))

area = (base * height)/2

print(f"The area of right angle triangle is : {int(area)}")    #converted to int value
'''