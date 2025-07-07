import turtle
from turtle import Turtle, Screen
import heroes

# Create turtle object
timmy = Turtle()
print(heroes.gen())

# ---------------- Short Way ---------------- #

# Define a function that draws any shape based on number of sides
timmy.shape("turtle")
colors = ["#FF6B6B","#FFA94D","#FFD93D","#6BCB77","#4D96FF","#845EC2","#D65DB1","#FF6F91"]

def draw_shape(num_sides, color):
    angle = 360 / num_sides
    timmy.color(color)
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

# Draw shapes from triangle (3 sides) to decagon (10 sides)
for i, shape_side_n in enumerate(range(3, 11)):
    draw_shape(shape_side_n, colors[i])


# ---------------- Long Way ---------------- #

# Each shape is drawn with its own function and loop
def triangle():
    timmy.color("#FF6B6B")
    timmy.forward(100)
    timmy.right(120)

for _ in range(3):
    triangle()

def square():
    timmy.color("#FFA94D")
    timmy.forward(100)
    timmy.right(90)

for _ in range(4):
    square()

def pentagon():
    timmy.color("#FFD93D")
    timmy.forward(100)
    timmy.right(72)

for _ in range(5):
    pentagon()

def hexagon():
    timmy.color("#6BCB77")
    timmy.forward(100)
    timmy.right(60)

for _ in range(6):
    hexagon()

def heptagon():
    timmy.color("#4D96FF")
    timmy.forward(100)
    timmy.right(51.4)

for _ in range(7):
    heptagon()

def octagon():
    timmy.color("#845EC2")
    timmy.forward(100)
    timmy.right(45)

for _ in range(8):
    octagon()

def nonagon():
    timmy.color("#D65DB1")
    timmy.forward(100)
    timmy.right(40)

for _ in range(9):
    nonagon()

def decagon():
    timmy.color("#FF6F91")
    timmy.forward(100)
    timmy.right(36)

for _ in range(10):
    decagon()

# Exit on click
screen = Screen()
screen.exitonclick()





