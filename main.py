import time
from turtle import Turtle, Screen

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)

all_turtles = []

is_game_on = True

for i in range(0, 3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(0 - (i*20), 0)

    all_turtles.append(new_turtle)


while is_game_on:
    my_screen.update()
    time.sleep(0.1)

    for num in range(len(all_turtles) - 1, 0, -1):
        new_x = all_turtles[num - 1].xcor()
        new_y = all_turtles[num - 1].ycor()

        all_turtles[num].goto(new_x, new_y)

    all_turtles[0].forward(20)


my_screen.exitonclick()