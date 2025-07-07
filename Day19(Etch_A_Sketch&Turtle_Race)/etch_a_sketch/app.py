from turtle import Turtle, Screen

# Create turtle and screen objects
timmy = Turtle()
screen = Screen()

# Movement functions mapped to keys
def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def turn_left():
    timmy.left(10) # Rotate turtle counter-clockwise


def turn_right():
    timmy.right(10) # Rotate turtle clockwise

# Clears the drawing and returns turtle to center
def clear_drawing():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

# Keybindings to control the turtle
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")

# Exit the window on click
screen.exitonclick()

