import pygame
import pygame.locals as pl
import sys

# Initialize pygame
pygame.init()

FPS = 60
clock = pygame.time.Clock()

# Screen information and constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple demo")

# --- Main Game Loop ---
while True:     
    for event in pygame.event.get():               
        if event.type == pl.QUIT:
            pygame.quit()
            sys.exit()
            
    # call move and/or update method of each sprite

    # check for collisions

    # end the loop
    pygame.display.update()
    clock.tick(FPS)
