from turtle import Turtle

# Font settings for displaying text on the screen
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    # Initializes the scoreboard with starting level and position
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    # Updates the scoreboard display with the current level
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    # Increases the level and refreshes the display
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    # Displays a "Game Over" message in the center of the screen
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)





