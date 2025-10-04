# Line of random stamps
import turtle
import random

random.seed()

my_turtle = turtle.Turtle()
turtle.mode('logo')
turtle.resizemode('auto')

myColourList = ['red', 'black', 'orange', 'blue', 'purple']
myShapeList = ['turtle', 'arrow', 'square', 'circle', 'triangle', 'classic']

def makeStamp():
    my_turtle.setheading(random.randint(1, 360))
    my_turtle.color(random.choice(myColourList))
    my_turtle.shape(random.choice(myShapeList))
    my_turtle.stamp()

# Main program
my_turtle.penup()

for i in range(10):
    makeStamp()
    my_turtle.setheading(90)
    my_turtle.forward(50)

turtle.done()
