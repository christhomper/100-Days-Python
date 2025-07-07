from turtle import Turtle

# Constants defining player movement and screen boundaries
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    # Initializes the player turtle with appearance and starting position
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.speed(0)
        self.go_to_start()
        self.setheading(90)

    # Moves the player upward by a fixed amount
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    # Sends the player back to the starting position
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    # Checks whether the player has reached the top of the screen
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False



