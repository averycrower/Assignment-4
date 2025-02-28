from turtle import *
import turtle
import math
import random

bgcolor("dark blue")
speed(0)
colormode(255)


# Draw spiral
for i in range(500):  # Number of loops for density
    pencolor(255 - i % 255, i % 255, (i * 2) % 255)  # Dynamic color change
    forward(i * 1.5)  # Spiral expansion
    right(89)  # Angle for swirl effect

# Background stars (optional effect)
penup()
for _ in range(50):  # Number of stars
    goto(random.randint(-400, 400), random.randint(-400, 400))
    dot(random.randint(2, 5), "white")  # Random size white dots
pendown()

turtle.done()

