import random

#generate random num 1-10
secret_number = random.randint(1,10)

# set guesses
guesses_left = 5
user_guess = 0

# main game
while guesses_left > 0:
    user_guess = input("Enter your guess (1-10): ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a valid number")
        continue

    if user_guess == secret_number:
        print(f"Congrats! Your guess {user_guess} was correct!")
        break
    elif user_guess > secret_number: 
        print("Too high!")
    else:
        print("Too low!")

    #reduce attempts and check for remaining guesses
    guesses_left -= 1

    if guesses_left == 0:
        print(f"Game over! The number was {secret_number}.")