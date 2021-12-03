from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


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

    def game_over(self, text="GameOver!",
                  alignment="center",
                  font=('Arial', 20, 'normal')):
        """GameOver Message"""
        self.home()
        self.write(arg=text, align=alignment, font=font)


