from turtle import Turtle, Screen

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")

all_turtles = []

for i in range(0, 3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.goto(0 - (i*20), 0)

    all_turtles.append(new_turtle)




my_screen.exitonclick()