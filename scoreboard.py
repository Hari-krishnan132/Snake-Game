from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('courier', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.pendown()
        self.write("Score: 0", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)