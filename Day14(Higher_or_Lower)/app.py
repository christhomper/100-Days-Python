from art import logo, vs
from game_data import data
import random

def format_data(account):
    """Takes an account dictionary and formats it into a printable string."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Compares follower counts and checks if the user's guess is correct."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

def game():
    """Runs one round of the Higher Lower game."""
    print(logo)
    score = 0
    game_should_continue = True
    # Start with a random account for B; A will be assigned on first loop.
    account_b = random.choice(data)

    while game_should_continue:
        # Carry over previous B to new A, then get a new B.
        account_a = account_b
        account_b = random.choice(data)

        # Ensure A and B are not the same
        if account_a == account_b:
            account_b = random.choice(data)

        # Display account info to user
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.\n")

        # Get user guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Clear screen effect
        print("\n" * 100)
        print(logo)

        # Retrieve follower counts
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # Check if guess is correct
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Handle result
        if is_correct:
            score += 1
            print(f"You're right! Current score {score}\n")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.\n")
            game_should_continue = False

# Replay loop for continuous play
while True:
    game()
    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    print("\n" * 100)
    if play_again != 'y':
        print("Thanks for playing! Goodbye 👋.")
        break
