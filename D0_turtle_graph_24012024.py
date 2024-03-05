import turtle as t
from turtle import Screen
import random

tim = t.Turtle()

tim.shape("turtle")
tim.color("green")
colors = ["Teal", "MediumSpringGreen", "lightSkyBlue", "Turquoise", "Cyan", "PaleGreen", "LightSeaGreen", "SeaGreen"]

for i in range(3,10):
    num_sides = i
    angle = 360 / num_sides
    tim.color(random.choice(colors))
    for i in range(1,num_sides + 1):
        tim.forward(40)
        tim.right(angle)

screen = Screen()
screen.exitonclick()
print(tim)