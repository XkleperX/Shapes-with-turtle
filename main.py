from turtle import Screen, Turtle, bgcolor
from os import system

system("cls")
import random

screen = Screen()
screen.colormode(255)
t = Turtle()
# t.shape("turtle")
t.speed("fastest")


def color():
    g = random.randint(0, 255)
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


bgcolor("black")


def draw_shape(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color("pink")
        t.circle(200)
        t.setheading(t.heading() + size_of_gap)


draw_shape(2)

screen.exitonclick()
