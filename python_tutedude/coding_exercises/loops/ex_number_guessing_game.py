"""
Create a simple number guessing game.
The user gets 10 chances to guess a number.
If the user guesses the number before 10 chances, stop asking the number from the user, say Congrats and end the game if the user never guesses a number, ask them 10 times and then end the game!!
""" 
'''
number = 25
attempts = 10
print("Welcome to the number guessing game. we have a number that needs to be guessed. \nYou have 10 chances.\nThe secret number between 1 to 50" )
while attempts > 0:

    correct_number = int(input("Enter your guess :"))
    

    if correct_number == number:
        print("Congrats your guess is correct!!")
        break
    elif correct_number < number:
        print("Your guess is wrong !! Try higher")
        attempts -= 1
        print(f"you have {attempts} left.")
    elif correct_number > number:
        print("Your guess is wrong !! Try lower")
        attempts -= 1
        print(f"you have {attempts} left.")

        
    else:
        print("Invalid Number!!")

else : 
    print(f"Bad Luck ! You couldn't guess \nThe secret number is {number}. Game Over !!")
'''


'''
# or you can write like this-->

import random

secret_number = random.randint(1, 100)
attempts = 5  # total attempts allowed

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print(f"You have {attempts} attempts to guess it.\n")

while attempts > 0:
    guess = int(input("Enter your guess: "))
    attempts -= 1

    if guess < secret_number:
        print("Too low!\n")
    elif guess > secret_number:
        print("Too high!\n")
    else:
        print("🎉 Correct! You guessed the number!")
        break

    print(f"Attempts left: {attempts}\n")

if attempts == 0:
    print("❌ Out of attempts! Better luck next time.")
    print(f"The correct number was: {secret_number}")

'''





# Below Code is referred from ChatGPT.
# Number Guessing Game with Difficulty Levels
# Difficulty Levels:
# Easy → number between 1–20 → 7 attempts
# Medium → number between 1–50 → 6 attempts
# Hard → number between 1–100 → 5 attempts

import random

print("🎯 Welcome to the Number Guessing Game!")
print("Choose a difficulty level:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

choice = input("Enter your choice (1/2/3): ")

# Setting range and attempts based on difficulty
if choice == "1":
    max_range = 20
    attempts = 7
elif choice == "2":
    max_range = 50
    attempts = 6
elif choice == "3":
    max_range = 100
    attempts = 5
else:
    print("Invalid choice! Defaulting to Easy mode.")
    max_range = 20
    attempts = 7

secret_number = random.randint(1, max_range)

print(f"\nI have selected a number between 1 and {max_range}.")
print(f"You have {attempts} attempts to guess it.\n")

while attempts > 0:
    guess = int(input("Enter your guess: "))
    attempts -= 1

    if guess < secret_number:
        print("Too low!\n")
    elif guess > secret_number:
        print("Too high!\n")
    else:
        print("🎉 Correct! You guessed the number!")
        break

    print(f"Attempts left: {attempts}\n")

if attempts == 0:
    print("❌ Out of attempts!")
    print(f"The correct number was: {secret_number}")
