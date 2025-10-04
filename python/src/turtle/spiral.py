import turtle  #Inside_Out
wn = turtle.Screen()
wn.bgcolor("light green")

my_turtle = turtle.Turtle()
my_turtle.color("blue")
my_turtle.pensize(3)

def sqrfunc(size):
    for i in range(4):
        my_turtle.fd(size)
        my_turtle.left(90)
        size = size + 5

sqr_size = 6
for i in range(20):
    sqrfunc(sqr_size)
    sqr_size = sqr_size + 20

turtle.done()
