# Python program to draw star
# using Turtle Programming
import turtle
my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.shapesize(2)
my_turtle.pensize(3)

my_turtle.right(75)
my_turtle.forward(100)

for i in range(4):
    my_turtle.right(144)
    my_turtle.forward(100)
    
turtle.done()
