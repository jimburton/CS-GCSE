import turtle
from turtle import Turtle

def draw_bar_chart(data: dict, labels: tuple, colours: list=None):
    """Draw a bar chart using the data in the dict and the colours in the list.
    
       Preconditions: the dict has string keys and numeric values.
       Postconditions: the pen will be in the up position.

    Args:
        data (dict): The data to draw.
    """
    the_turtle = Turtle()
    origin_x, origin_y = the_turtle.pos()
    # find largest value in dict 
    max = 0
    for val in data.values():
        if val > max:
            max = val
    # Add together the length of the labels
    length = 0
    for key in data.keys():
        length += len(key)
    length *= 10
    # draw the x axis
    the_turtle.pendown()
    the_turtle.setheading(90) # North
    the_turtle.forward(max)
    the_turtle.penup()
    the_turtle.setposition(origin_x, origin_y)
    # draw the y axis
    the_turtle.setheading(0) # East
    the_turtle.pendown()
    the_turtle.forward(length)
    the_turtle.penup()
    the_turtle.setposition(origin_x, origin_y)
    # draw the x axis label
    the_turtle.setheading(90) # North
    the_turtle.forward(max)
    the_turtle.setheading(180)
    the_turtle.forward(15)
    the_turtle.write(str(max))
    the_turtle.setheading(270) # South
    the_turtle.forward(max/2)
    the_turtle.setheading(180) # West
    the_turtle.forward(len(labels[0])*6)
    the_turtle.write(labels[0])
    # go back
    the_turtle.setposition(origin_x, origin_y)
    # draw y axis label
    the_turtle.setheading(0) # East
    the_turtle.forward(length/2)
    the_turtle.setheading(270) # South
    the_turtle.forward(50)
    the_turtle.write(labels[1])
    
    the_turtle.setposition(origin_x, origin_y)
    
    the_turtle.setheading(0) # East
    the_turtle.forward(10)
    # draw the bars
    count = 0
    colour = None
    for key,value in data.items():
        if colours:
            colour = colours[count%len(colours)]
            count += 1
        draw_bar(the_turtle, 10, value, colour, key)
        the_turtle.forward(10)
    turtle.done()
    
    
def draw_bar(the_turtle: Turtle, width: int, height:int, colour:str='#0000FF', label: str=None) -> None :
    """Draw a rectangle of the given width and height, filled with
       the given colour. The orientation will be set to East (0 degrees) 
       before drawing.
       
       Preconditions: width and height are positive integers, colour is a string
                      representing a colour. 
       Postconditions: A rectangle will be drawn with the correct dimensions and
                       filled with the given colour. The pen will be lifted after 
                       drawing and the orientation will be East (0 degrees).

    Args:
        the_turtle (Turtle): The turtle to do the drawing.
        width (int): The width of the bar.
        height (int): The height of the bar.
        colour (int): The colour of the bar.
    """
    the_turtle.setheading(0)
    the_turtle.pendown()
    the_turtle.begin_fill()
    the_turtle.color(colour)
    the_turtle.forward(width)
    the_turtle.left(90)
    the_turtle.forward(height)
    the_turtle.left(90)
    the_turtle.forward(width)
    the_turtle.left(90) 
    the_turtle.forward(height)
    the_turtle.end_fill()
    the_turtle.setheading(0)
    the_turtle.penup()
    offset = 10
    if label:
        # move below the bar to write the label
        the_turtle.color('#000000')
        the_turtle.right(90)
        the_turtle.forward(20)
        the_turtle.write(label)
        # go back and reset heading
        the_turtle.left(90)
        the_turtle.forward(20)
        the_turtle.left(90)
        the_turtle.forward(20)
        the_turtle.setheading(0)
        offset += len(label)*2
    the_turtle.forward(offset)
    
    