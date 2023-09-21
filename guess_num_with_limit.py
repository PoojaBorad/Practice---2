print("Modify the 'Guess the Number' game to allow the user to set a maximum number and a limited number of attempts.")

import random

def guess_number():
    print("Welcome to the Game of the 'GUESS THE NUMBER'!")
    print("I will choose a random number, and you have to guess it.")

    #max_number = int(input("Enter the maximum you want to guess: "))
    #Maximum nuber is already fixed.
    max_number = 100
    print(f"You have to guess the number between 1 to {max_number}!")
    max_attempts = int(input("Enter the number of attempts you want: "))

    secret_number = random.randint(1, max_number)
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int (input(f"Enter your guess number between 1 to {max_number}:"))
        except ValueError:
            print("Invalid Number. Please try again.")  
            continue

        attempts += 1
#Using f string insted of (.format) function.
        if guess < 1 or guess > max_number:
            print(f"Your guess is not valid (1 - {max_number}). Try again.")
        elif guess > secret_number:
            print("your guess is high! Try again.")
        elif guess < secret_number:
            print("Your guess is low! Try again.")  
        else: 
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")      
            break

    if attempts >= max_attempts:
        print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")

guess_number()       

        

