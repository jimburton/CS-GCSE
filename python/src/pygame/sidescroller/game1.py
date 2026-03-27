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
    # Resource loading
    run = [pygame.image.load(os.path.join('images', 'run_' + str(x) + '.png')) for x in range(8)]
    jump = [pygame.image.load(os.path.join('images', 'jump_' + str(x) + '.png')) for x in range(8)]
    slide = [pygame.image.load(os.path.join('images', 'slide_0.png'))] + \
        [pygame.image.load(os.path.join('images', 'slide_1.png')) for _ in range(7)] + \
        [pygame.image.load(os.path.join('images', 'slide_2.png')),
         pygame.image.load(os.path.join('images', 'slide_3.png')),
         pygame.image.load(os.path.join('images', 'slide_4.png'))]
    fall = pygame.image.load(os.path.join('images', 'fall.png'))
    jump_list = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,
                3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,
                -1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,
                -3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]

    def __init__(self):
        super().__init__() # Initialize the Sprite class
        self.x = 200
        self.y = 313
        self.width = 64
        self.height = 64
        self.jumping = False
        self.sliding = False
        self.falling = False
        self.slide_count = 0
        self.jump_count = 0
        self.run_count = 0
        self.slide_up = False
        
        # Initialize image, rect, and mask for collide_mask
        self.image = self.run[0]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, win):
        if self.falling:
            self.image = self.fall
            current_y = self.y + 30
        elif self.jumping:
            self.y -= self.jump_list[self.jump_count] * 1.3
            self.image = self.jump[self.jump_count // 18]
            self.jump_count += 1
            if self.jump_count > 108:
                self.jump_count = 0
                self.jumping = False
                self.run_count = 0
            current_y = self.y
        elif self.sliding or self.slide_up:
            if self.slide_count < 20:
                self.y += 1
            elif self.slide_count == 80:
                self.y -= 19
                self.sliding = False
                self.slide_up = True

            if self.slide_count >= 110:
                self.slide_count = 0
                self.run_count = 0
                self.slide_up = False
            
            self.image = self.slide[self.slide_count // 10]
            current_y = self.y
            self.slide_count += 1
        else:
            if self.run_count > 40:
                self.run_count = 0
            self.image = self.run[self.run_count // 8]
            self.run_count += 1
            current_y = self.y

        # Update the rect and mask based on the current animation frame and position
        self.rect.topleft = (self.x, current_y)
        self.mask = pygame.mask.from_surface(self.image)
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
