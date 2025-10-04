import turtle
# Create a turtle object
my_turtle = turtle.Turtle()
# Draw a square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)
# Save the Turtle graphic as an EPS file
turtle.getscreen().getcanvas().postscript(file="my_square.eps")
# Exit the turtle graphics window
turtle.done()
