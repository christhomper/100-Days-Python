from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def turn_left():
    # EASY WAY
    timmy.left(10)
    # HARD WAY
    # new_heading = timmy.heading() + 10
    # timmy.setheading(new_heading)

def turn_right():
    # EASY WAY
    timmy.right(10)
    # HARD WAY
    # new_heading = timmy.heading() - 10
    # timmy.setheading(new_heading)

def clear_drawing():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")
screen.exitonclick()

