import turtle

# Create a turtle object
my_turtle = turtle.Turtle()
my_turtle.speed(0.5)

# Set the pen color and size
my_turtle.pensize(3)
colors = ["red", "blue", "green", "orange"]

# Draw a circle pattern
for i in range(36):
    my_turtle.pencolor(colors[i % 4])
    my_turtle.circle(100)
    my_turtle.right(10)

# Exit the turtle graphics window
turtle.done()
