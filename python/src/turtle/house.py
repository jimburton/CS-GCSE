# Turtle program to draw square 
import turtle
my_turtle = turtle.Turtle()

for _ in range(4):
    my_turtle.forward(50) # draw the line
    my_turtle.right(90) # turn 90 degrees

# first side of roof
my_turtle.forward(50)
my_turtle.right(120)

# second side of roof
my_turtle.forward(50)
    
turtle.done()
