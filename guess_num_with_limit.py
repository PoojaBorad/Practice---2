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
            guess = int (input("Enter your guess number between 1 to {}: ".format(max_number)))
        except ValueError:
            print("Invalid Number. Please try again.")  
            continue

        attempts += 1

        if guess < 1 or guess > max_number:
            print("Your guess is not valid (1 - {}). Try again.".format(max_number))
        elif guess > secret_number:
            print("your guess is high! Try again.")
        elif guess < secret_number:
            print("Your guess is low! Try again.")  
        else: 
            print("Congratulations! You guessed the number {} in {} attempts.".format(secret_number, attempts))      
            break

    if attempts >= max_attempts:
        print("Sorry, you've run out of attempts. The secret number was {}.".format(secret_number))

guess_number()       

        

