from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial", 15, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("score_file.txt") as self.sc_file:
            self.content=self.sc_file.read()
        self.highest_score = int(self.content)
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.scrupdate()
        self.hideturtle()

    def scrupdate(self):
        self.clear()
        self.write(f"Score:{self.score} Highest Score : {self.highest_score} ", False, ALIGNMENT, FONT)
        with open("score_file.txt",mode="w") as self.sc_file:
            self.sc_file.write(str(self.highest_score))


    def reset(self):
        if self.score> self.highest_score:
            self.highest_score = self.score
        self.score=0
        self.scrupdate()



    def inc_scr(self):
        self.score+=1
        self.clear()
        self.scrupdate()

    # def hit_wall_msg(self):
    #     self.goto(0,0)
    #     self.write("HIT WALL", False, ALIGNMENT, FONT)


    # def hit_tail_msg(self):
    #     self.goto(0,0)
    #     self.write("COLLISION WITH TAIL", False, ALIGNMENT, FONT)
    #
    #
    # def clear_msg(self):
    #     self.clear()










