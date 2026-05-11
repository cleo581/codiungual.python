import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("rectangle")
white = (255,255,255)
blue=(0,0,255)
black=(0,0,0)
rect_width = 100
rect_height = 50
rect_x=(640-rect_width)//2
rect_y=(480-rect_height)//2
font = pygame.font.SysFont(None, 40)
text  = font.render("hello world", True, (0,0,0))
running = True
while running:
    screen.fill(white)

    pygame.draw.rect(screen,blue,(270,190,100,80))
    screen.blit(text, (280, 200))
    pygame.display.update()
    for event in pygame.event.get():
       if event.type == pygame.quit:
            running = False

    