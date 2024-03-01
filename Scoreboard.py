# TODO: 5- Create a score board
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.write(f"Score: {self.score}  HighScore: {self.high_score}", False, ALIGNMENT, FONT)

        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  HighScore: {self.high_score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
