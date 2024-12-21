import turtle
from turtle import Turtle
FONT_SCORE = ('Arial', 15, 'normal')
ALIGN ='center'
MOVE = False
FONT_GO = ('Arial', 25, 'normal')
FONT_REMATCH = ('Arial', 15, 'normal')

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=265)
        self.points = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.points}", move = MOVE, align = ALIGN, font = FONT_SCORE)
    def add_points(self):
        self.points += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=MOVE, align=ALIGN, font=FONT_GO)
        self.goto(0, -25)
        self. write(f"CLICK ENTER FOR REMATCH", move=MOVE, align=ALIGN, font=FONT_REMATCH)

    def reset_scoreboard(self):
        self.clear()




