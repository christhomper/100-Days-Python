from turtle import Turtle, Screen
import random

# Set up screen and race state
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

# Ask user to bet on a turtle color
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Define turtle colors and starting y-positions
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

# Create turtle racers
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Start the race if user placed a bet
if user_bet:
    is_race_on = True

# Race loop
while is_race_on:
    for turtle in all_turtles:
        # Check if turtle has crossed the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")

        # Move each turtle forward a random distance
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# Exit on click
screen.exitonclick()
