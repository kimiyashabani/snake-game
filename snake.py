from turtle import Turtle

# TODO: 1- Create a snake body
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.my_snake = []
        self.create_snake()
        self.head = self.my_snake[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_to_snake(position)

    def add_to_snake(self,position):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.my_snake.append(snake)
    def extend(self):
        #-1 is the last one
        self.add_to_snake(self.my_snake[-1].position())

    def move(self):
        for right in range(len(self.my_snake) - 1, 0, -1):
            new_x = self.my_snake[right - 1].xcor()
            new_y = self.my_snake[right - 1].ycor()
            self.my_snake[right].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def reset(self):
        for seg in self.my_snake:
            seg.goto(1000,1000)
        self.my_snake.clear()
        self.create_snake()
        self.head = self.my_snake[0]