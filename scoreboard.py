from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Goudy Stout", 8, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r"D:/Coding/Coding Languages/Python/Snake_Game/scorekeeper.txt") as highestscore:
            self.highscore = int(highestscore.read())
        self.highscore = 0
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.update()
    
    def update(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore :
            self.highscore = self.score
            with open(r"D:/Coding/Coding Languages/Python/Snake_Game/scorekeeper.txt", mode="w") as highestscore:
                highestscore.write(f"{self.highscore}")
        self.score = 0
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.update()


