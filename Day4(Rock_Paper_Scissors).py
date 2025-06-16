# Import the random module to allow the computer to make a random choice

import random


# Define ASCII art for Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Define ASCII art for Paper
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# Define ASCII art for Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List storing the ASCII art for each choice, indexed by 0 (rock), 1 (paper), 2 (scissors)
rps_art = [rock, paper, scissors]

# List storing the names of each choice, indexed by 0 (rock), 1 (paper), 2 (scissors)
rps_names = ["Rock", "Paper", "Scissors"]

# Get user input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Validate input
if user_choice < 0 or user_choice > 2:
    print("Invalid choice. You must enter 0, 1, or 2.")
else:
    computer_choice = random.randint(0,2)

    # Display the user's choice (name and ASCII art)
    print(f"\nYou chose: \n{rps_names[user_choice]}\n{rps_art[user_choice]}")
    # Display the computer's choice (name and ASCII art)
    print(f"\nComputer chose: \n{rps_names[computer_choice]}\n{rps_art[computer_choice]}")

    # Determine the outcome of the game:
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose.")










