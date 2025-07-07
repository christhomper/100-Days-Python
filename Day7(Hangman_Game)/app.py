import random
from hangman_words import word_list
from hangman_art import stages, logo

# Print game logo and initialize game state
print(logo)
lives = 6
chosen_word = random.choice(word_list)

# Set up word placeholder display
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# Main game loop
game_over = False
correct_letters = []

while not game_over:

    print((f"****************************{lives}/6 LIVES LEFT****************************"))
    guess = input("Guess a letter: ").lower()

    # Handle repeated guesses
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    # Update display based on current guess
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # Check for incorrect guesses and reduce lives
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word} YOU LOSE**********************")

    # Check for win condition
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Show hangman stage graphic
    print(stages[lives])
