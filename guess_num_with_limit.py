print("Modify the 'Guess the Number' game to allow the user to set a maximum number and a limited number of attempts.")

import random

def guess_number():
    print("Welcome to the Game of the 'GUESS THE NUMBER'!")
    print("I will choose a random number, and you have to guess it.")

    max_number = int(input("Enter the maximum you want to guess: "))
    max_attempts = int(input("Enter the number of attempts you want: "))

    secret_number = random.randint(1, max_number)
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int (input("Enter your guess number: ".format(max_number)))
        except ValueError:
            print("Invalid Number. Please try again.")  
            continue

        attempts += 1

        if guess < 1 or guess > max_number:
            print("Your guess is not valid. Try again.".format(max_number))
            

        

