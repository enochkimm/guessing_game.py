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

    #compare user_guess with secret_number
    IF user_guess is equal to secret_number THEN
        DISPLAY "Congratulations! Your guess of __ was correct!"
        EXIT the LookupError
    
    ELSE IF user_guess is greater than secret_number THEN
        Display "Too high! Try again."

    ELSE 
        DISPLAY "Too low! Try again."

    ENDIF 

    #reduce attempts and check for remaining guesses
    DECREASE guesses_left by 1

    IF guesses_left is equal to 0 THEN
        DISPLAY "Game over! The number was __! Thanks for playing!"