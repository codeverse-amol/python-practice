'''
>= 90 grade A
80 and 89 , grade B
70 and 79 , grade C
60 and 69 , grade D
< 60 , Fail
'''

# if-elif-else

marks = float(input("Enter your marks: "))

if marks >= 60:
    print("Congrats!, you passed the exam.")
    if marks >=90:
        print("Your grade is 'A'")
    elif  80 <= marks <= 89 :                   # standard way of writing condition.
        print("Your grade is 'B'")
    elif marks <= 79 and marks >= 70 :          # simple way
        print("Your grade is 'C'")
    else:
        print("Your grade is 'D'")
else:
    print("Failed!, you have to study hard.")