import turtle

# Set up the turtle screen and set the background color to yellowy brown
screen = turtle.Screen()
screen.bgcolor("goldenrod")

# Create a new turtle and set its speed to the fastest possible
my_turtle = turtle.Turtle()
my_turtle.speed(0)

# Set the fill color to red
my_turtle.fillcolor("red")
my_turtle.begin_fill()

# Draw the circle with a radius of 100 pixels
my_turtle.circle(100)

# End the fill and stop drawing
my_turtle.end_fill()

# draw a dot in the middle of the circle
my_turtle.color('white')
my_turtle.penup()
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.dot(20)
my_turtle.hideturtle()

# Keep the turtle window open until it is manually closed
turtle.done()
