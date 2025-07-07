from turtle import Turtle

# Constants for text alignment and font style
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):
    # Initializes the scoreboard with a starting score and position
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    # Displays the current score on the screen
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Displays the "Game Over" message at the center of the screen
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # Increases the score and refreshes the display
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


