import turtle
from turtle import Turtle, Screen
import random

# Create turtle
timmy = Turtle()
timmy.shape("turtle")
turtle.colormode(255) # Enable RGB color mode

# Generate a random RGB color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# Set turtle properties for the walk
direction = [0, 90, 180, 270]
timmy.pensize(10)
timmy.speed(0)

# Perform random walk
for _ in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(direction))

# Exit on click
screen = Screen()
screen.exitonclick()