from turtle import Turtle

class Ball(Turtle):
    # Initializes the ball's appearance, starting movement direction, and speed
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # Moves the ball based on its current direction
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Reverses the vertical direction (bounce off top/bottom wall)
    def bounce_y(self):
        self.y_move *= -1

    # Reverses the horizontal direction (bounce off paddle) and increases speed
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # Resets ball to center and restores speed after a point is scored
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()


