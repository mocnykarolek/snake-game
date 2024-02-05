from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreborad
#ustawienia ekranu
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
#obiekty
snake = Snake()
food = Food()
scoreboard = Scoreborad()

# nasluchuje klawisze
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
#  gra sie zaczyna
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.forward(20)
    if snake.head.distance(food) < 15:
        scoreboard.scored()
        food.refresh()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collinsion with the snake's body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
