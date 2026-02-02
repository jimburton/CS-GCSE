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
bg_x = 0
bg_x2 = bg.get_width()

clock = pygame.time.Clock()


def redraw_window():
    win.blit(bg, (bg_x, 0))
    win.blit(bg, (bg_x2, 0))
    runner.draw(win)

    pygame.display.update()

# Game Setup
EVENT_BG = pygame.event.custom_type()
pygame.time.set_timer(EVENT_BG, 500)

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__() # Initialize the Sprite class
        self.x = 200
        self.y = 313
        self.width = 64
        self.height = 64
        
        # Initialize image, rect, and mask for collide_mask
        self.image = pygame.image.load(os.path.join('images', '8.png'))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, win):
        win.blit(self.image, self.rect)
            
speed = 30
run = True
runner = Player()

# Main Game Loop
while run:
        
    score = speed // 10 - 3

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == EVENT_BG:
            speed += 1
            
    # Background scrolling
    bg_x -= 1.4
    bg_x2 -= 1.4

    if bg_x < bg.get_width() * -1:
        bg_x = bg.get_width()
    if bg_x2 < bg.get_width() * -1:
        bg_x2 = bg.get_width() 

    clock.tick(speed)
    redraw_window()

pygame.quit()
