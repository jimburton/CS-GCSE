import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
FPS = 60
GRAVITY = 0.8
JUMP_STRENGTH = -16
PLAYER_SPEED = 7
WATER_SPEED_START = 1.0
PLATFORM_GAP = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)
WATER_COLOR = (0, 105, 148, 180) # RGBA
GREEN = (34, 139, 34)
RED = (200, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 100))
        self.vel_y = 0
        self.score = 0

    def update(self, platforms):
        keys = pygame.key.get_pressed()
        dx = 0
        if keys[pygame.K_LEFT]:
            dx = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            dx = PLAYER_SPEED

        # Gravity
        self.vel_y += GRAVITY
        dy = self.vel_y

        # Horizontal boundaries
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > WIDTH:
            dx = WIDTH - self.rect.right

        # Collision with platforms (only while falling)
        for plat in platforms:
            if plat.rect.colliderect(self.rect.x + dx, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.vel_y > 0: # Falling
                    if self.rect.bottom <= plat.rect.top:
                        self.rect.bottom = plat.rect.top
                        dy = 0
                        self.vel_y = JUMP_STRENGTH # Auto-jump on platforms

        self.rect.x += dx
        self.rect.y += dy

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        super().__init__()
        self.image = pygame.Surface((width, 15))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rising Tide Climber")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24)

    # Sprite Groups
    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()

    # Initial Player
    player = Player()
    all_sprites.add(player)

    # Initial Platforms
    start_plat = Platform(0, HEIGHT - 20, WIDTH)
    all_sprites.add(start_plat)
    platforms.add(start_plat)

    for i in range(1, 8):
        p = Platform(random.randint(0, WIDTH - 70), HEIGHT - (i * PLATFORM_GAP), 70)
        all_sprites.add(p)
        platforms.add(p)

    water_y = HEIGHT + 100
    water_speed = WATER_SPEED_START
    scroll = 0
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and game_over:
                main() # Restart
                return

        if not game_over:
            player.update(platforms)
            
            # Water rises
            water_y -= water_speed
            # Speed up water slightly as player scores
            water_speed = WATER_SPEED_START + (player.score / 5000)

            # Camera Scroll logic
            if player.rect.top <= HEIGHT // 3:
                diff = HEIGHT // 3 - player.rect.top
                player.rect.y += diff
                water_y += diff
                for plat in platforms:
                    plat.rect.y += diff
                player.score += diff

            # Generate new platforms
            last_plat = min(platforms, key=lambda p: p.rect.y)
            if last_plat.rect.y > PLATFORM_GAP:
                new_p = Platform(random.randint(0, WIDTH - 70), last_plat.rect.y - PLATFORM_GAP, 70)
                all_sprites.add(new_p)
                platforms.add(new_p)

            # Delete off-screen platforms
            for plat in platforms:
                if plat.rect.top > HEIGHT:
                    plat.kill()

            # Game Over check
            if player.rect.top >= water_y or player.rect.top > HEIGHT:
                game_over = True

        # Drawing
        screen.fill(SKY_BLUE)
        all_sprites.draw(screen)

        # Draw Water (with transparency)
        water_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(water_surface, WATER_COLOR, (0, water_y, WIDTH, HEIGHT))
        screen.blit(water_surface, (0, 0))

        # Score UI
        score_text = font.render(f"Score: {int(player.score)}", True, BLACK)
        screen.blit(score_text, (10, 10))

        if game_over:
            over_text = font.render("GAME OVER! Press any key.", True, BLACK)
            screen.blit(over_text, (WIDTH // 2 - 120, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
