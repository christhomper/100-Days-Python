import turtle
import random
from turtle import Turtle, Screen

# Create turtle
timmy = Turtle()
turtle.colormode(255)
timmy.speed(0)

# Generate random RGB color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# Draw a full spirograph by rotating circle with color
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

# Call the spirograph function
draw_spirograph(5)

# Exit on click
screen = Screen()
screen.exitonclick()
