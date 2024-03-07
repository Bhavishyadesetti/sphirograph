import turtle
from turtle import Turtle,Screen
from random import randint
tim=Turtle()
tim.width(2)
tim.speed("fastest")
turtle.colormode(255)

angle =5
while angle<361:
    col=(randint(0,255),randint(0,255),randint(0,255))
    tim.pencolor(col)
    tim.circle(100)
    tim.setheading(angle)
    angle+=5




screen=Screen()
screen.exitonclick()