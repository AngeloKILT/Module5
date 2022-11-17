# Angelo Smith
# 11/3/2022
# This code only lets you make a shape with any number but you are given these two shapes to make a triangle or square
print("Please enter 90 for sides if you want a square")
print("Please enter 120 for sides if you want a triangle")
Shape = input("Enter a shape")
Sides = int(input("Enter a sides"))
Color = input("Enter a color")
import turtle
Tom = turtle.Turtle()
Tom.pencolor("blue")
Tom.fillcolor(Color)
Tom.begin_fill()
for num in range(5):
    Tom.forward(Sides)
    Tom.left(Sides)
    Tom.forward(Sides)
Tom.end_fill()