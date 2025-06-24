from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
NORMAL_LEVEL_TURNS = 7
HARD_LEVEL_TURNS = 5
EXTREME_LEVEL_TURNS = 3
SUDDEN_DEATH_LEVEL_TURNS = 1

# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high 👇")
        return turns -1
    elif user_guess < actual_answer:
        print("Too low 👆")
        return turns -1
    else:
        print(f"You win 😃! The answer is {actual_answer}")

# Function to set difficulty
def set_difficulty():
    """Sets difficulty for number guessing game."""
    level = input("Choose a difficulty. Type 'easy' , 'normal' , 'hard' , 'extreme' or 'sudden death': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "normal":
        return NORMAL_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    elif level == "extreme":
        return EXTREME_LEVEL_TURNS
    else:
        return SUDDEN_DEATH_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()

    # Repeat the guessing functionality if player gets it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts left to guess the number.")
        # Let the player guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if player gets it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose 😭.")
            return
        elif guess != answer:
            print("Guess again.")

game ()

while True:
    game()
    play_again = input("Do you want to play again? Type 'y' for yes or 'n' to quit: ")
    if play_again != 'y':
        print("Thanks for playing! Goodbye 👋.")
        break










