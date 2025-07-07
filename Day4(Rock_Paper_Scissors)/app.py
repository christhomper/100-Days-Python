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

# Store the ASCII art for each option in a list (index 0 = rock, 1 = paper, 2 = scissors)
rps_art = [rock, paper, scissors]

# Store the corresponding names for easier readability in output
rps_names = ["Rock", "Paper", "Scissors"]

# Ask user to choose between Rock, Paper, or Scissors
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Check if the user's choice is valid
if user_choice < 0 or user_choice > 2:
    print("Invalid choice. You must enter 0, 1, or 2.")
else:
    # Generate random choice for computer
    computer_choice = random.randint(0,2)

    # Display user and computer choices (name and ASCII)
    print(f"\nYou chose: \n{rps_names[user_choice]}\n{rps_art[user_choice]}")
    print(f"\nComputer chose: \n{rps_names[computer_choice]}\n{rps_art[computer_choice]}")

    # Determine and print the result
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose.")










