from random import randint
from art import logo
print(logo)

EASY_LIVES = 10
HARD_LIVES = 5

# Prompt user for "easy" or "hard"
#   easy = 10 lives, hard = 5 lives
def player_lives():
    difficulty = input("Choose difficulty (easy)/hard : ").lower()
    if difficulty == "hard":
        return HARD_LIVES
    else:
        return EASY_LIVES


# Pick random number from 1 to 100
def ai_number():
    print("I have thought of a number between 1 and 100.")
    return randint(1, 100)


#   Prompt player for guess
def player_guess():
    return int(input("Make a guess : "))


# Compare player guess to AI number
def check_guess(_guess, _number, _lives, _game_over):
    if _guess == _number:
        print(f"You got it! The number was {_number}")
        _game_over = True
    else:
        # Reduce lives by 1 
        _lives -= 1
        # Check for last life
        if _lives == 0:
            print("You Lose. No lives remaining.")
            _game_over = True

#       Else tell player if number is too high, low
        else:
            if _guess > _number:
                print("Too high.\n\nGuess again.")
            else:
                print("Too low.\n\nGuess again.")
            print(f"You have {_lives} lives remaining to guess the number.")
    # Return multiple values
    return _lives, _game_over


# START
# =====
def game():
    guess = 0
    lives = player_lives()
    number = ai_number()
    game_over = False

    while not game_over:
        guess = player_guess()
        # Function check_guess() returns multiple values
        result = check_guess(guess, number, lives, game_over)
        lives = result[0]
        game_over = result[1]


game()