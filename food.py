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

    def new_food(self):
        """It set Food and Food Position"""
        coordinates = (
            float(randint(-275, 275)),
            float(randint(-275, 265))
            )
        self.goto(coordinates)
        self.food_position = coordinates

    def is_food_eat(self, snake):
        """Return Bool value"""
        if snake.distance(self.food_position) < pixel:
            self.new_food()
            return True
        else:
            return False
