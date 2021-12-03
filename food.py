from turtle import Turtle
from random import randint

pixel = 10


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
        if snake_object.distance(self.food_position) < pixel:
            self.new_food()
            return True
        else:
            return False
