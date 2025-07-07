# Display ASCII art title
print("""
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
""")

# Introduction and mission
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
cross_road = input('You\'re at a cross road. Where do you want to go?\n'
                   'Type "left" or "right".\n').lower()

# First choice: Crossroad
if cross_road == "right":
    # Bad ending if player chooses right
    print("You fell into a canyon. Game Over.")
elif cross_road == "left":
    # Second choice: Lake
    lake = input('You\'ve come to a lake. There is an island in the middle of the lake.\n'
                 'Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if lake == "swim":
        # Bad ending if player chooses to swim
        print('You were attacked by piranhas. Game Over.')
    elif lake == "wait":
        # Final choice: House with doors
        house = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n'
                      'Type "red", "yellow" or "blue"\n').lower()
        if house == "red":
            print('You were attacked by pirates. Game Over.')
        elif house == "blue":
            print('You tripped a mine. Game Over.')
        elif house == "yellow":
            print('You found the treasure! You Win!')
        else:
            print("That door doesn't exist. Game Over.")

    else:
        # If player enters something unexpected at lake
        print("You hesitated too long and got dragged into the lake by sirens. Game Over.")

else:
    # If player enters something unexpected at the crossroad
    print("You stood there unsure where to go. A snake bit you. Game Over.")









