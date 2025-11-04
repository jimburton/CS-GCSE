# tell Python we want to use the turtle library
import turtle

# make a turtle
my_turtle = turtle.Turtle()
my_turtle.shape('turtle')

count = 0

# draw a square for the main part of the house
my_turtle.fillcolor('blue')
my_turtle.begin_fill()
while count < 4: 
    my_turtle.forward(100)
    my_turtle.right(90)
    count = count + 1
my_turtle.end_fill()


# draw a triangle for the roof of the house
my_turtle.fillcolor('green')
my_turtle.begin_fill()

my_turtle.left(60)
my_turtle.forward(100)
my_turtle.right(120)
my_turtle.forward(100)

my_turtle.end_fill()

# move to the right place to draw the door 
my_turtle.penup()
my_turtle.goto(50,-100)
my_turtle.left(150)

# draw the door
my_turtle.pendown()
my_turtle.fillcolor('white')
my_turtle.begin_fill()
my_turtle.forward(25)
my_turtle.right(90)
my_turtle.forward(10)
my_turtle.right(90)
my_turtle.forward(25)
my_turtle.end_fill()

turtle.done()





