print("Modify the 'Guess the Number' game to allow the user to set a maximum number and a limited number of attempts.")

import random

def guess_number():
    print("Welcome to the Game of the 'GUESS THE NUMBER'!")
    print("I will choose a random number, and you have to guess it.")

    max_number = int(input("Enter the maximum you want to guess: "))
    max_attempts = int(input("Enter the number of attempts you want in this game between 1 to 15: "))

    secret_number = random.randint(1, max_number)
    attempts = 0

    