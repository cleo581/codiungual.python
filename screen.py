import pygame
import sys
pygame.init()
width= 800
hieght = 600

screen = pygame.display.set_mode((width,hieght))
pygame.display.set_caption("my first game screen")
white=(255,255,255)
blue= (0,100,255)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()
sys.exit()
    