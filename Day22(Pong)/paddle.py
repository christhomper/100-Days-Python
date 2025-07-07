from turtle import Turtle

class Paddle(Turtle):
    # Initializes the paddle with size, color, and starting position
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    # Moves the paddle upward by 20 pixels
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # Moves the paddle downward by 20 pixels
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




