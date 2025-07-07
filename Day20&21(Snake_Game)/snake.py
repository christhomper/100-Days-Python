from turtle import Turtle

# Constants for initial snake setup and movement directions
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    # Initializes the snake with starting segments and sets the head
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Creates the initial snake body
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Adds a new segment to the snake at a given position
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("aquamarine3")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Extends the snake by adding a segment at the tail
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Moves the snake forward by updating each segment's position
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Change direction to up unless currently going down
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Change direction to down unless currently going up
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Change direction to left unless currently going right
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Change direction to right unless currently going left
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



