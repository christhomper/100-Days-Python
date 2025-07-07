# Uncomment this section to extract colors from an image using colorgram
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("hirst_image.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

# Set up turtle color mode to accept RGB values from 0–255
turtle_module.colormode(255)

# Create turtle object
timmy = turtle_module.Turtle()
timmy.speed(0)  # Fastest drawing speed
timmy.penup()  # Lift the pen so it doesn't draw lines between dots
timmy.hideturtle()  # Hide the turtle cursor

# List of RGB color tuples (extracted from image using colorgram)
color_list = [(242, 233, 237), (186, 160, 139), (143, 166, 178), (148, 173, 156), (122, 94, 83),
              (183, 148, 158), (126, 81, 91), (81, 107, 125), (218, 202, 145), (86, 111, 96),
              (167, 105, 118), (174, 105, 95), (214, 178, 186), (175, 202, 186), (218, 180, 172),
              (102, 144, 116), (89, 142, 156), (143, 136, 98), (170, 200, 207), (114, 43, 54),
              (184, 189, 203), (117, 124, 146), (46, 54, 67), (62, 55, 50), (66, 51, 61),
              (97, 51, 46), (49, 61, 85)]

# Move turtle to starting position (bottom left corner of grid)
timmy.setheading(220)  # Face diagonally down-left
timmy.forward(310)     # Move into position
timmy.setheading(0)    # Face right

# Total number of dots to draw
number_of_dots = 100

# Loop through and draw each dot
for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))  # Draw a colored dot
    timmy.forward(50)  # Move forward to next dot position

    # After every 10 dots, move up to start a new row
    if dot_count % 10 == 0:
        timmy.setheading(90)  # Face up
        timmy.forward(50)     # Move up one row
        timmy.setheading(180) # Face left
        timmy.forward(500)    # Move back to the start of the row
        timmy.setheading(0)   # Face right again

# Keep the window open until clicked
screen = turtle_module.Screen()
screen.exitonclick()
