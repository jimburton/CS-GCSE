"""Demo of drawing a triangle in Python."""
import turtle

my_turtle = turtle.Turtle()

def draw_triangle(the_turtle, side_length):
    """Draw a triangle."""
    for i in range(3):
        the_turtle.forward(side_length)
        the_turtle.right(120)

my_turtle.pensize(3)
my_turtle.color('blue')
my_turtle.left(60)
draw_triangle(my_turtle, 100)

turtle.done()
        
