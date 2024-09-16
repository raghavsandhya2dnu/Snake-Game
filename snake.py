from turtle import Turtle

SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP=90
RIGHT=0
LEFT=180
DOWN=270

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in SNAKE_POSITION:
            snake_segment = Turtle("square")
            snake_segment.color("green")
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments.append(snake_segment)

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_new = self.segments[seg_num - 1].xcor()
            y_new = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_new, y_new)
        self.segments[0].forward(MOVE_DISTANCE)



    def move_up(self):
        if self.segments[0].heading()!=DOWN:
            self.segments[0].setheading(UP)

    def move_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def move_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def move_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)


    def add_new_seg(self):
        x_pos=self.segments[-1].xcor()
        y_pos = self.segments[-1].ycor()
        snake_segment = Turtle("square")
        snake_segment.color("green")
        snake_segment.penup()
        snake_segment.goto(x_pos,y_pos)
        self.segments.append(snake_segment)







