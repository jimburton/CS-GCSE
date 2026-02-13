import pygame
import pygame.locals as pl
import sys

# Initialize pygame
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Screen information and constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BAT_WIDTH = 10
BAT_HEIGHT = 200
BLOCK_SIZE = 30
BLOCK_MOTION = 5

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple demo")

FONT_START_SCREEN = pygame.font.SysFont("Comic Sans Ms", 50)
LABEL_START = FONT_START_SCREEN.render("Enter 1 or 2 for a one or two player game", True, WHITE)

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        # Draw a white square
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.x_dir = -1 # -1 = right to left, 1 = left to right
        self.y_dir = -1 # -1 = up, 1 = down
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        # bounce
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.y_dir *= -1
        if self.rect.left <= BAT_WIDTH or self.rect.right >= SCREEN_WIDTH - BAT_WIDTH:
            self.x_dir *= -1
        # move
        self.rect.move_ip(BLOCK_MOTION * self.x_dir, BLOCK_MOTION * self.y_dir)

class Bat(pygame.sprite.Sprite):
    def __init__(self, player=False, two_player=False):
        super().__init__()
        self.player = player
        self.two_player = two_player
        # Draw a white bat
        self.image = pygame.Surface((50, 200))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        starting_x = BAT_WIDTH / 2 if self.player else SCREEN_WIDTH - (BAT_WIDTH / 2)
        self.rect.center = (starting_x, SCREEN_HEIGHT / 2)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, block_y=None):
        if self.player:
            pressed_keys = pygame.key.get_pressed()
            if self.rect.top > 0:
                if pressed_keys[pl.K_UP]:
                    self.rect.move_ip(0, -5)
            if self.rect.bottom < SCREEN_HEIGHT:        
                if pressed_keys[pl.K_DOWN]:
                    self.rect.move_ip(0, 5)
        elif self.two_player:
            pressed_keys = pygame.key.get_pressed()
            if self.rect.top > 0:
                if pressed_keys[pl.K_w]:
                    self.rect.move_ip(0, -5)
            if self.rect.bottom < SCREEN_HEIGHT:        
                if pressed_keys[pl.K_s]:
                    self.rect.move_ip(0, 5)
        else:
            self.follow(block_y)

    def follow(self, block_y):
        print(f"{block_y=}, {self.rect.centery=}")
        y_delta = 5 
        if block_y > self.rect.centery: # move bat down
            if self.rect.bottom + y_delta < SCREEN_HEIGHT:
                self.rect.move_ip(0, y_delta)
        elif block_y < self.rect.centery: # move bat up
            y_delta *= -1
            if self.rect.top > 0:
                self.rect.move_ip(0, y_delta)

# Setup groups and objects
block = Block()
bat1 = Bat(player=True)
bat2 = Bat(player=False)

# --- Main Game Loop ---
def game_loop():
    while True:     
        for event in pygame.event.get():               
            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()
            
        # Update logic
        bat1.update()
        bat2.update(block.rect.centery)
        block.update()
    
        # Drawing
        win.fill(BLACK)
        block.draw(win)
        bat1.draw(win)
        bat2.draw(win)

        pygame.display.update()
        FramePerSec.tick(FPS)

def start_screen():
    global bat2
    while True:     
        for event in pygame.event.get():               
            if event.type == pl.KEYDOWN and event.key == pl.K_1:
                bat2 = Bat(player=False, two_player=False)
                game_loop()
            elif event.type == pl.KEYDOWN and event.key == pl.K_2:
                bat2 = Bat(player=False, two_player=True)
                game_loop()
            
        # Drawing
        win.fill(BLACK)
        win.blit(LABEL_START, (100,100))

        pygame.display.update()
        FramePerSec.tick(FPS)

if __name__ == '__main__':
    start_screen()
