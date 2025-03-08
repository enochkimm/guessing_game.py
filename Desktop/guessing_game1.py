IMPORT the random module

#generate random num 1-10
SET secret_number TO random int between 1 and 10

# set guesses
SET guesses_left to %
SET user_guess to 0

# main game
WHILE guesses_left is greater than 0 DO:

    #prompt user guess
    DISPLAY "Enter your guess (1-10):"
    GET user input and CONVERT to integer
    STORE input in user_guess

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