'''
>= 90 grade A
80 and 89 , grade B
70 and 79 , grade C
60 and 69 , grade D
< 60 , Fail

'''

# if-elif-else

marks = float(input("Enter your marks: "))

if marks >=90:
    print("Passed with grade 'A'")
elif  80 <= marks <= 89 :                   # standard way of writing condition.
    print("Passed with grade 'B'")
elif marks <= 79 and marks >= 70 :          # simple way
    print("Passed with grade 'C'")
elif marks <= 69 and marks >= 60 :
    print("Passed with grade 'D'")
else:
    print("Failed")