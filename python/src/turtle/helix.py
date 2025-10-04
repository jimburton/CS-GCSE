# Python program to draw 
# Spiral  Helix Pattern
# using Turtle Programming

import turtle
#loadWindow = turtle.Screen()

my_turtle = turtle.Turtle()
my_turtle.speed(0.5)

colours = ['blue', 'gold', 'maroon', 'red', 'pink', 'orange']

for i in range(100):
    #my_turtle.color(colours[i % 5])
    my_turtle.circle(5*i)
    my_turtle.circle(-5*i)
    my_turtle.left(i)

turtle.done()
