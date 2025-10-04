# Python program to draw square 
# using Turtle Programming
import turtle
my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.speed(1)

def draw_house(t):
    for _ in range(4):
        t.forward(50) # draw the line
        t.right(90) # turn 90 degrees

    # first side of roof
    t.right(-60)
    t.forward(50)


    # second side of roof
    t.right(120)
    t.forward(50)

draw_house(my_turtle)
my_turtle.up() # lift the pen
my_turtle.forward(250)
my_turtle.down() # put the pen down
draw_house(my_turtle)

my_turtle.up() # lift the pen
my_turtle.setx(0)
my_turtle.sety(50)
my_turtle.down() # out the pen down
my_turtle.write("Hello world", font=("Arial", 32, "normal"))

turtle.done()
