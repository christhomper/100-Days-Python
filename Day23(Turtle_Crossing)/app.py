import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the game window and initialize screen settings
screen = Screen()
screen.title("Shell Dash")
screen.setup(width=600, height=600)
screen.tracer(0)

# Instantiate the player, car manager, and scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Set up user input to control the player
screen.listen()
screen.onkey(player.go_up, "Up")

# Start the main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Manage car generation and movement
    car_manager.create_car()
    car_manager.move_cars()

    # Check for collisions between the player and any car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Check if player has successfully crossed the screen
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

# Exit the game on screen click
screen.exitonclick()