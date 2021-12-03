from turtle import Turtle
from random import randint

start_point = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
segment_between_space = 15
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
SPEED = 0
PIXEL = 10
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Snake:

    def __init__(self):
        self.snake_segment = []
        self.snake_body()
        self.head = self.snake_segment[0]
        self.head.shape("triangle")
        self.tail = self.snake_segment[2:]

    def snake_body(self):
        """Return Snake Segment object"""
        for pos in start_point:
            self.add_segment(pos)

    def add_segment(self, position,
                    shape="square",
                    color="black",
                    length=0.5,
                    width=0.5):
        """Add segment"""
        snakes = Turtle(shape=shape)
        snakes.color(color)
        snakes.turtlesize(stretch_len=length, stretch_wid=width)
        snakes.penup()
        snakes.goto(position)
        self.snake_segment.append(snakes)

    def extend(self):
        """ADD Segment at Last Segment Position"""
        self.add_segment(self.snake_segment[-1].position())

    def move(self):
        """Return Snake Head Position and
           Move Snake Forward"""
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
        """Move Snake Up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        """Move Snake Right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        """Move Snake Down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):
        """Reset Snake"""
        for seg in self.snake_segment:
            seg.goto(1000, 1000)
        self.__init__()

    @staticmethod
    def snake_boundary(head_position,
                       x_positive=300,
                       x_negative=-300,
                       y_positive=300,
                       y_negative=-300):
        """Return Bool value"""
        if head_position[0] > x_positive or head_position[0] < x_negative or head_position[1] > y_positive \
                or head_position[1] < y_negative:
            return False
        else:
            return True


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.turtlesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.food_position = ()
        self.new_food()

    def new_food(self, x_pos_border=275,
                 x_neg_border=-275,
                 y_pos_border=275,
                 y_neg_border=-275):
        """Make Food and Set Food Position"""
        x = x_pos_border
        minus_x = x_neg_border
        y = y_pos_border
        minus_y = y_neg_border
        coordinates = (
            float(randint(minus_x, x)),
            float(randint(minus_y, y))
            )
        self.goto(coordinates)
        self.food_position = coordinates

    def is_food_eat(self, snake_object):
        """Return Bool value"""
        if snake_object.distance(self.food_position) < PIXEL:
            self.new_food()
            return True
        else:
            return False


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.scoreboard_coordinates = (0.00, 270)
        self.scoreboard_body(coordinate=self.scoreboard_coordinates)

    def scoreboard_body(self, alignment=ALIGNMENT,
                        font=FONT,
                        coordinate=None):
        """Scoreboard Body"""
        self.clear()
        self.setposition(coordinate)
        self.write(arg=f"[ Score : {self.score}  HighScore : {self.high_score} ]", align=alignment, font=font)

    def increase_score(self):
        """Increase ScoreBoard"""
        self.score += 1
        self.scoreboard_body(coordinate=self.scoreboard_coordinates)

    def reset(self):
        """Reset ScoreBoard"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.scoreboard_body(coordinate=self.scoreboard_coordinates)

    def game_over(self, text="GameOver!", alignment="center", font=('Arial', 20, 'normal')):
        """GameOver Message"""
        self.home()
        self.write(arg=text, align=alignment, font=font)
