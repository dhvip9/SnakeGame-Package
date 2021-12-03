import turtle

start_point = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
segment_between_space = 15
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
PIXEL = 10
SPEED = 0


class Snake:

    def __init__(self):
        self.snake_segment = []
        self.snake_body()
        self.head = self.snake_segment[0]
        self.head.shape("triangle")
        self.tail = []

    def snake_body(self):
        """Return Snake Segment object"""
        for pos in start_point:
            self.add_segment(pos)

    def add_segment(self, position):
        """add segment"""
        snakes = turtle.Turtle("square")
        snakes.color("red")
        snakes.turtlesize(stretch_len=0.5, stretch_wid=0.5)
        snakes.penup()
        snakes.goto(position)
        self.snake_segment.append(snakes)

    def extend(self):
        """ADD Segment"""
        self.add_segment(self.snake_segment[-1].position())

    def move(self):
        """Return Movement of Snake"""
        for seg_num in range(len(self.snake_segment) - 1, 0, -1):
            x_coordinate = self.snake_segment[seg_num - 1].xcor()
            y_coordinate = self.snake_segment[seg_num - 1].ycor()
            self.snake_segment[seg_num].goto(x_coordinate, y_coordinate)
        self.head.forward(segment_between_space)
        return self.head.position()

    def right(self):
        """Move Snake Right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        """Move Snake Left"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        """Move Snake Right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        """Move Snake Left"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):
        """Reset Snake"""
        for seg in self.snake_segment:
            seg.goto(1000, 1000)
        self.__init__()

    @staticmethod
    def snake_boundary(position):
        """Return Bool value"""
        if position[0] > 290 or position[0] < -290 or position[1] > 280 or position[1] < -290:
            return False
        else:
            return True
