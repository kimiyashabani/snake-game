from turtle import Screen
from snake import Snake
from food import Food
from Scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("snake game")
screen.bgcolor("black")
screen.tracer(0)

# TODO: 2- Move our snake
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # TODO: 4- Detect collision with food
    if snake.head.distance(food) < 15:
        food.random_food()
        snake.extend()
        score.increase_score()
    # TODO: 6- Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    # TODO: 7- Detect collision with tail
    for segment in snake.my_snake[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()



screen.exitonclick()
