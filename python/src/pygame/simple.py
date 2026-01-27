import pygame
import pygame.locals as pl
import sys
import random

# Initialize pygame
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Screen information
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SuperPang!")

# --- Missing Arrow Class ---
class Arrow(pygame.sprite.Sprite):
    def __init__(self, x_pos):
        super().__init__()
        # Creating a simple vertical line surface to represent the arrow/bullet
        self.image = pygame.Surface((5, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x_pos
        self.rect.bottom = 520 # Starts at the player height

    def update(self):
        self.rect.y -= 10
        # Remove if it goes off screen
        if self.rect.bottom < 0:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        # Placeholder for player.png: a blue square
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 550)
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pl.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[pl.K_RIGHT]:
                self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Balloon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        # Placeholder for balloon.png: a green circle
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.image, GREEN, (20, 20), 20)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0) 
 
    def move(self):
        self.rect.move_ip(0, 5)
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.centerx = random.randint(40, SCREEN_WIDTH-40)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Setup groups and objects
P1 = Player()
B1 = Balloon()
arrows = pygame.sprite.Group()

# --- Main Game Loop ---
while True:     
    for event in pygame.event.get():               
        if event.type == pl.QUIT:
            pygame.quit()
            sys.exit()
        
        # Check for mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left click
                print("Click detected at:", event.pos)
                # Fire an arrow
                new_arrow = Arrow(P1.rect.centerx)
                arrows.add(new_arrow)
    
    # Update logic
    P1.update()
    B1.move()
    arrows.update()
     
    # Drawing
    DISPLAYSURF.fill(WHITE)
    P1.draw(DISPLAYSURF)
    B1.draw(DISPLAYSURF)
    
    # Draw all arrows in the group
    for arrow in arrows:
        DISPLAYSURF.blit(arrow.image, arrow.rect)
         
    pygame.display.update()
    FramePerSec.tick(FPS)
