import pygame
import pygame.locals as pl
import sys

# Initialize pygame
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Screen information
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple demo")

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        # Draw a blue square
        self.image = pygame.Surface((40, 40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 550)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Setup groups and objects
block = Block()

# --- Main Game Loop ---
while True:     
    for event in pygame.event.get():               
        if event.type == pl.QUIT:
            pygame.quit()
            sys.exit()
    
    # Update logic
     
    # Drawing
    DISPLAYSURF.fill(BLACK)
    block.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)
