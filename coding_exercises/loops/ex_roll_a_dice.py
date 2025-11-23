"""
Write a program to simulate a roll of a die/dice
A die has 6 faces with numbers 1 to 6 written on them
The program should randomly prints a number between 1 to 6

"""

import random

print("Welcome to the game!")

while True:
    choice  = input("Press 'Enter' to play or 'q' for exit :")
    
    if choice == 'q':
        print("Thank you for playing game, bye!!")
    elif choice == '':
        numbers = random.randint(1,6)
        print(f"Your number is {numbers}")
    else :
        print("Invalid input!!")

print("GAME OVER!!")