from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier', 24, "normal")

class Scoreborad(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreboard = Turtle()
        self.ht()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", False, ALIGNMENT, FONT)

    def game_over(self):
        self.home()
        self.write("Game over...", False, "center", FONT)

    def scored(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
