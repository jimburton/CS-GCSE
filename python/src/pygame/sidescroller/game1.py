"""
Sidescrolling game demonstrating scrolling background and sprite animation
with pixel-perfect mask collision detection.
"""
import pygame
import os
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 437
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Side Scroller')

bg = pygame.image.load(os.path.join('images', 'bg.png')).convert()
bg_x = 0
bg_x2 = bg.get_width()

clock = pygame.time.Clock()


def redraw_window():
    large_font = pygame.font.SysFont('comicsans', 30)
    win.blit(bg, (bg_x, 0))
    win.blit(bg, (bg_x2, 0))
    text = large_font.render('Score: ' + str(score), 1, (255, 255, 255))
    runner.draw(win)
    win.blit(text, (700, 10))
    pygame.display.update()

# Game Setup
EVENT_BG = pygame.USEREVENT + 1
pygame.time.set_timer(EVENT_BG, 500)

class Player(pygame.sprite.Sprite):
    run = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(8,16)]
    jump = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(1,8)]
    slide = [pygame.image.load(os.path.join('images', 'S1.png')),
             pygame.image.load(os.path.join('images', 'S2.png')),
             pygame.image.load(os.path.join('images', 'S2.png')),
             pygame.image.load(os.path.join('images', 'S2.png')),
             pygame.image.load(os.path.join('images', 'S2.png')),
             pygame.image.load(os.path.join('images', 'S2.png')),
             pygame.image.load(os.path.join('images', 'S2.png')),
             pygame.image.load(os.path.join('images', 'S2.png')),
             pygame.image.load(os.path.join('images', 'S3.png')),
             pygame.image.load(os.path.join('images', 'S4.png')),
             pygame.image.load(os.path.join('images', 'S5.png'))]
    fall = pygame.image.load(os.path.join('images','0.png'))
    jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,
                3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,
                -1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,
                -3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]

    def __init__(self):
        self.x = 200
        self.y = 313
        self.width = 64
        self.height = 64
        self.jumping = False
        self.sliding = False
        self.falling = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False

    def draw(self, win):
        if self.falling:
            win.blit(self.fall, (self.x, self.y + 30))

        elif self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.3
            win.blit(self.jump[self.jumpCount//18], (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            self.hitbox = (self.x+4, self.y, self.width-24, self.height-10)
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 1
                self.hitbox = (self.x+4, self.y, self.width-24, self.height-10)
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            elif self.slideCount > 20 and self.slideCount < 80:
                self.hitbox = (self.x, self.y+3, self.width-8, self.height-35)

            if self.slideCount >= 110:
                self.slideCount = 0
                self.runCount = 0
                self.slideUp = False
                self.hitbox = (self.x+4, self.y, self.width-24, self.height-10)
            win.blit(self.slide[self.slideCount//10], (self.x, self.y))
            self.slideCount += 1

        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount//6], (self.x, self.y))
            self.runCount += 1
            self.hitbox = (self.x+4, self.y, self.width-24, self.height-13)
            
speed = 30
score = 0
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

    if not runner.falling:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if not(runner.jumping):
                runner.jumping = True

        if keys[pygame.K_DOWN]:
            if not(runner.sliding):
                runner.sliding = True
                
    clock.tick(speed)
    redraw_window()

pygame.quit()
