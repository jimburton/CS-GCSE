import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)

def draw_square(the_turtle, side_length):
    for i in range(4):
        the_turtle.forward(side_length)
        the_turtle.left(90)

my_turtle.pensize(3)

for i in range(36):
    draw_square(my_turtle, 200)
    my_turtle.left(10)
    
#my_turtle.color('red')

#for i in range(36):
#    draw_square(my_turtle, 100)
#    my_turtle.left(10)

turtle.done()
