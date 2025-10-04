# Python program to draw square 
# using Turtle Programming
import turtle
t = turtle.Turtle()

def draw_house():
    # first side of house
    t.forward(50) # draw the line
    t.right(90) # turn 90 degrees

    # second side of house
    t.forward(50)
    t.right(90)

    # third side of house
    t.forward(50)
    t.right(90)

    # fourth side of house
    t.forward(50)
    t.right(30)
    
    # first side of roof
    t.forward(50)
    t.right(120)

    # second side of roof
    t.forward(50)

draw_house()
t.up() # lift the pen
t.forward(250)
t.down() # put the pen down
draw_house()

turtle.done()
