from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(x=0.00, y=270)
        self.score = 0
        with open("high_score.txt") as data:
            self.high_score = int(data.read())
        self.score_body()

    def score_body(self):
        """Set Score Body"""
        self.clear()
        self.write(arg=f"[ Score : {self.score}  HighScore : {self.high_score} ]", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Set Scoreboard Increase"""
        self.score += 1
        self.score_body()

    def reset(self):
        """Reset ScoreBoard"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.score_body()

    def game_over(self):
        """Set GameOver Message"""
        self.home()
        self.write(arg="GameOver!", align=ALIGNMENT, font=FONT)


