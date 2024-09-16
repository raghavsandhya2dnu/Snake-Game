import time
from turtle import Screen
#import playsound
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food= Food()
scboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)

screen.onkey(key="Left", fun=snake.move_left)

screen.onkey(key="Right", fun=snake.move_right)

screen.onkey(key="Down", fun=snake.move_down)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()
    #Detect collision with food
    if snake.head.distance(food)<15:
        scboard.inc_scr()
        snake.add_new_seg()
        food.refresh()

    #Detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        snake.reset()
        scboard.reset()


    #Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scboard.reset()
            snake.reset()







screen.exitonclick()
