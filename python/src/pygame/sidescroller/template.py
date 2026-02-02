"""
Sidescrolling game demonstrating scrolling background and sprite animation
with pixel-perfect mask collision detection.
"""
import pygame
import os

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 437
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Side Scroller')

bg = pygame.image.load(os.path.join('images', 'bg.png')).convert()

# TODO
# create two variables, bg_x and bg_x2, to store the current x position of two
# copies of the bg image 

clock = pygame.time.Clock()


def redraw_window():
    # TODO
    # draw bg twice, once at bg_x and once at bg_x2
    pygame.display.update()

# TODO
# create an event that will fire every 500 milliseconds

speed = 30
run = True

# Main Game Loop
while run:
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False            
        # TODO
        # if your custom event fires, increment speed
            
    # Background scrolling
    # TODO
    # subtract some figure from bg_x and bg_x2, moving them both to the left

    # if either bg image is no longer on screen, movit it all the way to the right
    # to start again.

    clock.tick(speed)
    redraw_window()

pygame.quit()
