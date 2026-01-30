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

class Player(pygame.sprite.Sprite):
    # Resource loading
    run = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(8, 16)]
    jump = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(1, 8)]
    slide = [pygame.image.load(os.path.join('images', 'S1.png'))] + \
        [pygame.image.load(os.path.join('images', 'S2.png')) for _ in range(7)] + \
        [pygame.image.load(os.path.join('images', 'S3.png')),
         pygame.image.load(os.path.join('images', 'S4.png')),
         pygame.image.load(os.path.join('images', 'S5.png'))]
    fall = pygame.image.load(os.path.join('images', '0.png'))
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
            if self.run_count > 42:
                self.run_count = 0
            self.image = self.run[self.run_count // 6]
            self.run_count += 1
            current_y = self.y

        # Update the rect and mask based on the current animation frame and position
        self.rect.topleft = (self.x, current_y)
        self.mask = pygame.mask.from_surface(self.image)
        win.blit(self.image, self.rect)

class Saw(pygame.sprite.Sprite):
    rotate = [pygame.image.load(os.path.join('images', 'SAW0.png')),
              pygame.image.load(os.path.join('images', 'SAW1.png')),
              pygame.image.load(os.path.join('images', 'SAW2.png')),
              pygame.image.load(os.path.join('images', 'SAW3.png'))]

    def __init__(self):
        super().__init__()
        self.x = 810
        self.y = 310
        self.width = 64
        self.height = 64
        self.rotateCount = 0
        
        # Initial image, rect, and mask
        self.image = pygame.transform.scale(self.rotate[0], (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, win):
        if self.rotateCount >= 8:
            self.rotateCount = 0
        
        # Update animation frame
        self.image = pygame.transform.scale(self.rotate[self.rotateCount // 2], (self.width, self.height))
        self.rect.topleft = (self.x, self.y)
        # Update mask for rotating objects
        self.mask = pygame.mask.from_surface(self.image)
        
        win.blit(self.image, self.rect)
        self.rotateCount += 1

class Spike(Saw):
    img = pygame.image.load(os.path.join('images', 'spike.png'))

    def __init__(self):
        super().__init__()
        self.x = 810
        self.y = 0
        self.width = 48
        self.height = 310
        self.image = self.img
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, win):
        self.rect.topleft = (self.x, self.y)
        # Masks for static images don't necessarily need to be regenerated every frame
        win.blit(self.image, self.rect)

def update_file():
    try:
        with open('scores.txt', 'r') as f:
            file_content = f.readlines()
            last = int(file_content[0])
    except FileNotFoundError:
        last = 0

    if last < int(score):
        with open('scores.txt', 'w') as f:
            f.write(str(score))
        return score
    return last

def end_screen():
    global pause, score, speed, obstacles
    pause = 0
    speed = 30
    obstacles = []

    run_end = True
    while run_end:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run_end = False
                runner.falling = False
                runner.sliding = False
                runner.jumping = False
                
        win.blit(bg, (0,0))
        large_font = pygame.font.SysFont('comicsans', 80)
        last_score = large_font.render('Best Score: ' + str(update_file()), 1, (255,255,255))
        current_score = large_font.render('Score: '+ str(score), 1, (255,255,255))
        win.blit(last_score, (SCREEN_WIDTH/2 - last_score.get_width()/2, 150))
        win.blit(current_score, (SCREEN_WIDTH/2 - current_score.get_width()/2, 240))
        pygame.display.update()
    score = 0

def redraw_window():
    large_font = pygame.font.SysFont('comicsans', 30)
    win.blit(bg, (bg_x, 0))
    win.blit(bg, (bg_x2, 0))
    text = large_font.render('Score: ' + str(score), 1, (255, 255, 255))
    
    runner.draw(win)
    for obstacle in obstacles:
        obstacle.draw(win)

    win.blit(text, (700, 10))
    pygame.display.update()

# Game Setup
EVENT_BG = pygame.USEREVENT + 1
EVENT_OBSTACLE = pygame.USEREVENT + 2
pygame.time.set_timer(EVENT_BG, 500)
pygame.time.set_timer(EVENT_OBSTACLE, 3000)

speed = 30
score = 0
run = True
runner = Player()
obstacles = []
pause = 0
fallSpeed = 0

# Main Game Loop
while run:
    if pause > 0:
        pause += 1
        if pause > fallSpeed * 2:
            end_screen()
        
    score = speed // 10 - 3

    for obstacle in obstacles:
        # Use pixel-perfect mask collision detection
        if pygame.sprite.collide_mask(runner, obstacle):
            runner.falling = True
            if pause == 0:
                pause = 1
                fallSpeed = speed
        
        if obstacle.x < -100:
            obstacles.pop(obstacles.index(obstacle))
        else:
            obstacle.x -= 1.4

    # Background scrolling
    bg_x -= 1.4
    bg_x2 -= 1.4

    if bg_x < bg.get_width() * -1:
        bg_x = bg.get_width()
    if bg_x2 < bg.get_width() * -1:
        bg_x2 = bg.get_width() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == EVENT_BG:
            speed += 1
            
        if event.type == EVENT_OBSTACLE:
            r = random.randrange(0, 2)
            if r == 0:
                obstacles.append(Saw())
            elif r == 1:
                obstacles.append(Spike())

    if not runner.falling:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if not runner.jumping:
                runner.jumping = True
        if keys[pygame.K_DOWN]:
            if not runner.sliding:
                runner.sliding = True

    clock.tick(speed)
    redraw_window()

pygame.quit()
