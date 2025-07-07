from turtle import Turtle
import random

class Food(Turtle):
    # Initializes the food as a small, colored turtle that appears on screen
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("bisque")
        self.speed("fastest")
        self.refresh() # Place the food at a random location initially

    # Moves the food to a new random location on the screen
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)