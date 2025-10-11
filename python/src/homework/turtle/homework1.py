import turtle

my_turtle = turtle.Turtle()

def draw_square(the_turtle, side_length):
    for i in range(4):
        the_turtle.forward(side_length)
        the_turtle.left(90)

my_turtle.pensize(3)

# draw the outer square
draw_square(my_turtle, 100)

# lift the pen up and move inside the first square
my_turtle.penup()
my_turtle.forward(10)
my_turtle.left(90)
my_turtle.forward(10)
my_turtle.right(90)

# put the pen down and draw the inner square
my_turtle.pendown()
draw_square(my_turtle, 80)

turtle.done()
