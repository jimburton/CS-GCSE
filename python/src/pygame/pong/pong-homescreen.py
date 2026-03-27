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

# game information
BAT_SPEED1 = 10
bat_speed2 = 8
BAT_WIDTH = 20
BAT_HEIGHT = 100
BALL_SPEED = 5
BALL_SIZE = 20
player_score = 0
computer_score = 0

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#events and timers
EVENT_SCORE = pygame.event.custom_type()
INTERVAL_SCORE = 3000
#
global in_play
in_play = True
global loading
loading = True

class Bat(pygame.sprite.Sprite):
    def __init__(self,is_player = True,two_player:bool = False):
        super().__init__()
        self.image = pygame.Surface((BAT_WIDTH,BAT_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.is_player = is_player
        self.two_player = two_player
        if self.is_player:
            self.rect.center = (BAT_WIDTH/2, SCREEN_HEIGHT/2)
        else:
            self.rect.center = (SCREEN_WIDTH - (BAT_WIDTH/2), SCREEN_HEIGHT/2)

    def draw(self,surface):
        """ draws the sprite"""
        surface.blit(self.image,self.rect)

    def update(self,ball_y = None):
        """ updates the sprite position(moves it)"""
        keys = pygame.key.get_pressed()
        if self.is_player:
            if keys[pl.K_UP]and self.rect.top > 0:
                self.rect.move_ip(0,-BAT_SPEED1)
            elif keys[pl.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
                self.rect.move_ip(0,BAT_SPEED1)

        elif self.two_player:
             if keys[pl.k_w]and self.rect.top > 0:
                self.rect.move_ip(0,-BAT_SPEED1)
             elif keys[pl.k_s] and self.rect.bottom < SCREEN_HEIGHT:
                self.rect.move_ip(0,BAT_SPEED1)

        else:
            if ball_y > self.rect.centery:

                self.rect.move_ip(0,computer_speed)
            elif ball_y < self.rect.centery:
                self.rect.move_ip(0,-computer_speed)
                
            
class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_SIZE,BALL_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        self.x_dir = -1
        self.y_dir = -1
        self.speed = BALL_SPEED
    def draw(self,surface):
        """ draws the sprite"""
        surface.blit(self.image,self.rect)

    def move(self):
        global player_score,computer_score, in_play,computer_speed
        #computer_speed = bat_speed2
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            pygame.mixer.Sound.play(hit_sound)
            self.y_dir *= -1
        if self.rect.left < 0:
            computer_score += 1
            pygame.mixer.Sound.play(score_sound)
        elif self.rect.right > SCREEN_WIDTH:
            player_score += 1
            computer_speed += 2
            pygame.mixer.Sound.play(score_sound)
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            #print (" scored a point")
            pygame.time.set_timer(EVENT_SCORE,INTERVAL_SCORE)
            in_play = False        
        self.rect.move_ip(self.speed* self.x_dir,self.speed*self.y_dir)
        
computer_speed = bat_speed2                                  
bat1 = Bat()
bat2 = Bat(is_player=False)
ball = Ball()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pong")
def reset():
    global in_play
    in_play = True
    ball.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    ball.speed = BALL_SPEED
    bat1.rect.centery = SCREEN_HEIGHT/2
    bat2.rect.centery = SCREEN_HEIGHT/2

def loading_screen():
    #my_font2 = pygame.font.Font("Jersey25-Regular.ttf",25)
    my_font2 = pygame.font.SysFont("Comic Sans MS",25)
    in_play = False
    while True:
        for event in pygame.event.get():               
            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pl.KEYDOWN and event.key == pl.K_2:
                bat2 = Bat(is_player=False, two_player=True)
                in_play = True
                play_game()
            elif event.type == pl.KEYDOWN and event.key == pl.K_1:
                bat2 = Bat(is_player=False, two_player=False)
                in_play = True
                play_game()
        if loading: 
            
            # draw the background and each sprite
            DISPLAYSURF.fill(BLACK)
            global pong
            pong =  my_font.render(f"pong",True,WHITE)
            one_p = my_font2.render(f"(single player: press 1)",True,WHITE)
            two_p =  my_font2.render(f"(two player: press 2)",True,WHITE)
            text_width = pong.get_rect().width/2
            text_height = pong.get_rect().height/2
            onep_width = one_p.get_rect().width/2
            onep_height = one_p.get_rect().height/2
            twop_width = two_p.get_rect().width/2
            twop_height = two_p.get_rect().height/2
            my_font.render(f"pong",True,WHITE)
            DISPLAYSURF.blit(pong,(SCREEN_WIDTH/2 - text_width,10 ))
            DISPLAYSURF.blit(one_p,(SCREEN_WIDTH/2 - onep_width,SCREEN_HEIGHT/4 ))
            DISPLAYSURF.blit(two_p,(SCREEN_WIDTH/2 - twop_width,SCREEN_HEIGHT/4 + twop_height*2 ))
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
        #    print (" k2 working")
        #    bat2 = Bat(player=False, two_player=False)
        #    in_play = True
        #    play_game()
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
        #    print (" k2 working")
        #    bat2 = Bat(player=False, two_player=True)
        #    in_play = True
        #    play_game()

        # end the loop
        pygame.display.update()
        clock.tick(FPS)


    
# --- Main Game Loop ---
#my_font = pygame.font.Font("Jersey25-Regular.ttf",100)
my_font = pygame.font.SysFont("Comic Sans MS",100)
hit_sound = pygame.mixer.Sound("pong_audio/hit.mp3")
score_sound = pygame.mixer.Sound("pong_audio/score.mp3")
def play_game():
    while True:
        for event in pygame.event.get():               
            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == EVENT_SCORE and not in_play:
                print ("detected our event")
                print (computer_speed)
                reset()
                
        if in_play:
            
            # call move and/or update method of each sprite
            bat1.update()
            bat2.update(ball.rect.centery)
            ball.move()
            # check for collisions then move the ball out of any bat collisions
            # this avoids the ball getting stuck to the bat
            if pygame.sprite.collide_mask(bat1,ball):
                ball.x_dir *= -1
                ball.rect.left = bat1.rect.right
                pygame.mixer.Sound.play(hit_sound)
                ball.speed += 1
                
            elif pygame.sprite.collide_mask(bat2,ball) :
                ball.x_dir *= -1
                ball.rect.right = bat2.rect.left
                pygame.mixer.Sound.play(hit_sound)
                ball.speed += 1

            # draw the background and each sprite
            DISPLAYSURF.fill(BLACK)
            bat1.draw(DISPLAYSURF)
            bat2.draw(DISPLAYSURF)
            ball.draw(DISPLAYSURF)
        else:
            
            scores_text = my_font.render(f"{player_score}|{computer_score}",True,WHITE)
            text_width = scores_text.get_rect().width/2
            text_height = scores_text.get_rect().height/2
            DISPLAYSURF.blit(scores_text,(SCREEN_WIDTH/2 - text_width,SCREEN_HEIGHT/2 - text_height))
    
    

        # end the loop
        pygame.display.update()
        clock.tick(FPS)

loading_screen()

