import turtle

# --- Setup the Turtle Screen ---
# Create the screen and set its properties
screen = turtle.Screen()
screen.setup(width=800, height=400)
screen.title("TIDE: Different Colors")
screen.bgcolor("lightgray") # Optional: a background color

# Create the turtle object
t = turtle.Turtle()
t.speed(0) # '0' is the fastest speed
t.hideturtle() # Make the turtle invisible during drawing

# Define starting position (left side of the screen)
t.penup()
t.goto(-200, -200)
t.pendown()

# Define the size of the letters (unit size)
UNIT = 50

# --- Function to Draw Each Letter ---
def draw_t(t, color):
    """Draws the letter T and fills it with the specified color."""
    t.color("black", color)
    t.begin_fill()

    # 1. Start at the bottom-left of the vertical stem
    
    # 2. Draw the vertical stem (going up)
    t.setheading(90) # Face up
    t.forward(UNIT * 4) # Full height
    
    # 3. Move to the end of the crossbar (going left)
    t.left(90) # Face left
    t.forward(UNIT) # Move to the left end of the crossbar
    
    # 4. Draw the perimeter of the crossbar and stem, moving clockwise
    t.right(90) # Face down
    t.forward(UNIT) # Move down (inner corner of T)
    
    t.right(90) # Face right
    t.forward(UNIT * 3) # The full width of the crossbar
    
    t.right(90) # Face up
    t.forward(UNIT) # Move up (inner corner of T)
    
    t.right(90) # Face left
    t.forward(UNIT) # Move to the right end of the crossbar

    # 5. Complete the path back to the start (bottom)
    t.left(90) # Face down
    t.forward(UNIT * 4) # Draw the right side of the vertical stem

    t.end_fill()
    
def draw_i(t, color):
    """Draws the letter I and fills it with the specified color."""
    t.color("black", color)
    t.begin_fill()

    # Draw the main vertical bar
    t.left(90)
    t.forward(UNIT * 4)
    t.right(90)
    t.forward(UNIT)
    t.right(90)
    t.forward(UNIT * 4)
    t.right(90)
    t.forward(UNIT)

    t.end_fill()
    t.right(90) # Reorient for the next letter

def draw_d(t, color):
    """Draws the letter D and fills it with the specified color."""
    t.color("black", color)
    t.begin_fill()

    # Draw the main vertical bar
    t.left(90)
    t.forward(UNIT * 4)
    t.right(90)
    t.forward(UNIT)
    t.right(90)
    t.forward(UNIT * 4)
    t.right(90)
    t.forward(UNIT)
    t.end_fill()
    
    # Move to the arc starting point (top right corner of the rectangle)
    #t.penup()
    #t.forward(UNIT)
    #t.right(90)
    #t.forward(UNIT * 4)
    #t.left(90)
    #t.pendown()

    # Draw the D shape using a circle/arc approximation (simpler approach)
    # This is a simplification; a smooth arc is more complex with turtle
    t.penup()
    t.right(180)
    t.forward(UNIT)
    t.pendown()

    t.begin_fill()
    t.circle(100, extent=180) # Draw half a circle to form the curve
    t.left(90)

    #t.end_fill()
    t.end_fill()
    t.penup()
    t.right(90) # Reorient for the next letter


def draw_e(t, color):
    """Draws the letter E and fills it with the specified color."""
    t.color("black", color)
    t.begin_fill()

        # Draw the main vertical bar
    t.left(90)
    t.forward(UNIT + (UNIT * 4))
    t.right(90)
    t.forward(UNIT)
    t.right(90)
    t.forward(UNIT + (UNIT * 4))
    t.right(90)
    t.forward(UNIT)
    t.end_fill()

    # Bottom bar
    t.penup()
    t.goto(t.xcor()+UNIT, t.ycor()+UNIT)
    t.pendown()
    t.begin_fill()
    t.setheading(0)
    t.forward(UNIT * 2)
    t.right(90)
    t.forward(UNIT)
    t.right(90)
    t.forward(UNIT * 2)
    t.end_fill()
    
    # Middle bar segment
    t.penup()
    t.goto(t.xcor(), t.ycor()+UNIT*3)
    t.pendown()
    t.begin_fill()
    t.setheading(0)
    t.forward(UNIT * 2)
    t.right(90)
    t.forward(UNIT)
    t.right(90)
    t.forward(UNIT * 2)
    t.end_fill()
    
    # Top bar
    t.penup()
    t.goto(t.xcor(), t.ycor()+UNIT*3)
    t.pendown()
    t.begin_fill()
    t.setheading(0)
    t.forward(UNIT * 2)
    t.right(90)
    t.forward(UNIT)
    t.right(90)
    t.forward(UNIT * 2)
    
    # Complete the shape (return to start of spine)

    t.end_fill()

# --- Drawing the Word TIDE ---

# 1. Draw T (Red)
draw_t(t, "red")

t.penup()
t.goto(-UNIT * 2, 0)
t.pendown()

# 2. Draw I (Blue)
t.forward(UNIT * 3) # Move space between letters
t.setheading(0)
draw_i(t, "blue")

t.penup()
t.goto(t.xcor() + UNIT * 2, -150)
t.pendown()

# 3. Draw D (Green)
#t.forward(UNIT * 2) # Move space between letters
t.setheading(0)
draw_d(t, "green")

t.penup()
t.goto(t.xcor(), -150)
t.pendown()

# 4. Draw E (Yellow)
t.setheading(0)
t.forward(UNIT * 3) # Move space between letters

draw_e(t, "yellow")

# --- Keep the Window Open ---
screen.mainloop()
