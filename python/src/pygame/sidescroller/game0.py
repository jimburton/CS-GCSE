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
    pygame.display.update()

# Game Setup
EVENT_BG = pygame.event.custom_type()
pygame.time.set_timer(EVENT_BG, 500)

speed = 30
score = 0
run = True

# Main Game Loop
while run:
        
    score = speed // 10 - 3

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False            
        elif event.type == EVENT_BG:
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
