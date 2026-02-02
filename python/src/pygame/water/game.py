import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
FPS = 60
GRAVITY = 0.8
JUMP_STRENGTH = -18  # Slightly stronger jump for better gameplay
PLAYER_SPEED = 7
WATER_SPEED_START = 1.2
PLATFORM_GAP = 110

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

        # Apply Gravity
        self.vel_y += GRAVITY
        dy = self.vel_y

        # Horizontal movement and boundaries
        self.rect.x += dx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        # Vertical movement and platform collision
        # We check collision BEFORE applying vertical movement to catch the landing
        if self.vel_y > 0:  # Only check if falling
            for plat in platforms:
                if plat.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                    # Check if the player was above the platform before the move
                    if self.rect.bottom <= plat.rect.top + 10: # 10px buffer for high speeds
                        self.rect.bottom = plat.rect.top
                        self.vel_y = JUMP_STRENGTH
                        dy = 0
                        break
        
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

    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()

    # Initial Player
    player = Player()
    all_sprites.add(player)

    # Base Platform
    base_plat = Platform(0, HEIGHT - 20, WIDTH)
    all_sprites.add(base_plat)
    platforms.add(base_plat)

    # Generate initial set of platforms
    for i in range(1, 10):
        p = Platform(random.randint(0, WIDTH - 70), HEIGHT - (i * PLATFORM_GAP), 70)
        all_sprites.add(p)
        platforms.add(p)

    water_y = HEIGHT + 50
    water_speed = WATER_SPEED_START
    game_over = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and game_over:
                main() # Restart
                return

        if not game_over:
            player.update(platforms)
            
            # Water rises and speed increases
            water_y -= water_speed
            water_speed = WATER_SPEED_START + (player.score / 10000)

            # Camera Scroll (Keep player in center)
            if player.rect.top <= HEIGHT // 2:
                scroll_amt = HEIGHT // 2 - player.rect.top
                player.rect.y += scroll_amt
                water_y += scroll_amt
                player.score += scroll_amt
                for plat in platforms:
                    plat.rect.y += scroll_amt

            # Generate new platforms as we climb
            highest_plat = min(platforms, key=lambda p: p.rect.y)
            if highest_plat.rect.y > 0:
                new_p = Platform(random.randint(0, WIDTH - 70), highest_plat.rect.y - PLATFORM_GAP, 70)
                all_sprites.add(new_p)
                platforms.add(new_p)

            # Cleanup old platforms
            for plat in platforms:
                if plat.rect.top > HEIGHT + 100:
                    plat.kill()

            # Check Loss Conditions
            if player.rect.top >= water_y or player.rect.top > HEIGHT:
                game_over = True

        # Rendering
        screen.fill(SKY_BLUE)
        all_sprites.draw(screen)

        # Draw Translucent Water
        water_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        # Ensure water_y doesn't go negative or break rect drawing
        draw_y = max(0, min(HEIGHT, water_y))
        pygame.draw.rect(water_surface, WATER_COLOR, (0, draw_y, WIDTH, HEIGHT - draw_y))
        screen.blit(water_surface, (0, 0))

        # UI
        score_text = font.render(f"Altitude: {int(player.score // 10)}m", True, BLACK)
        screen.blit(score_text, (10, 10))

        if game_over:
            msg = font.render("DROWNED! Press any key to retry", True, BLACK)
            screen.blit(msg, (WIDTH // 2 - 140, HEIGHT // 2))

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
