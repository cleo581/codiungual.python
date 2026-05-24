import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 400))

CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)

sprite1_color = (255, 0, 0)
sprite2_color = (0, 0, 255)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == CHANGE_COLOR:
            sprite1_color = (
                random.randint(0,255),
                random.randint(0,255),
                random.randint(0,255)
            )

            sprite2_color = (
                random.randint(0,255),
                random.randint(0,255),
                random.randint(0,255)
            )

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, sprite1_color, (100, 150, 80, 80))
    pygame.draw.rect(screen, sprite2_color, (300, 150, 80, 80))

    pygame.display.update()

pygame.quit()