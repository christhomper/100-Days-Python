from turtle import Turtle

class Scoreboard(Turtle):
    # Initializes the scoreboard with default scores and display settings
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    # Updates the score display for both players
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 40, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 40, "normal"))

    # Increases the left player's score and updates the display
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    # Increases the right player's score and updates the display
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()