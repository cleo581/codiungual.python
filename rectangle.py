import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (255,125,0),pygame.Rect(60,90,90,90))
    pygame.display.flip()
pygame.quit()
