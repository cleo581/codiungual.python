import pygame
import random

# Initialise pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader Game")

# Colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Player
player = pygame.Rect(375, 500, 50, 50)
player_speed = 5

# Create 7 enemies in random positions
enemies = []

for i in range(7):
    enemy = pygame.Rect(
        random.randint(0, WIDTH - 50),
        random.randint(0, HEIGHT - 50),
        50,
        50
    )
    enemies.append(enemy)

# Score
score = 0

# Font
font = pygame.font.SysFont(None, 40)

# Clock
clock = pygame.time.Clock()

# Main game loop
running = True

while running:

    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= player_speed

    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    if keys[pygame.K_UP]:
        player.y -= player_speed

    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # Keep player on screen
    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH

    if player.top < 0:
        player.top = 0

    if player.bottom > HEIGHT:
        player.bottom = HEIGHT

    # Collision detection
    for enemy in enemies:
        if player.colliderect(enemy):
            score += 1

            # Move enemy to a new random position
            enemy.x = random.randint(0, WIDTH - 50)
            enemy.y = random.randint(0, HEIGHT - 50)

    # Draw background
    screen.fill(WHITE)

    # Draw player
    pygame.draw.rect(screen, BLUE, player)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Draw score
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # FPS
    clock.tick(60)

pygame.quit()
