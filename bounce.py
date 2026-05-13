import pygame
import random
pygame.init()
sprite_colour_change_event = pygame.USEREVENT +1
background_colour_change_event = pygame.USEREVENT +2
blue = pygame.Color("blue")
lightblue = pygame.Color("lightblue")
darkblue = pygame.Color("darkblue")
yellow = pygame.Color("yellow")
magenta = pygame.Color("magenta")
orange = pygame.Color("orange")
white = pygame.Color("white")
class Sprite(pygame.sprite.Sprite):
    def __init__(self,colour,height,width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self,self.velocity)
        boundry_hit = False
        if self.rect.left < 0 or self.rect.right > 500:
            self.velocity[0] = -self.velocity[0]
            boundry_hit = True
        if self.rect.top < 0 or self.rect.bottom > 400:
            self.velocity[1] = -self.velocity[1]
            boundry_hit = True
        if boundry_hit:
            pygame.event.post(pygame.event.Event(sprite_colour_change_event))
            pygame.event.post(pygame.event.Event(background_colour_change_event))
    def change_colour(self):
        self.image.fill(random.choice([orange,magenta,lightblue,darkblue]))
def change_background_colour():
    global bg_colour 
    bg_colour = random.choice([blue,yellow,white])
allspritelist = pygame.sprite.Group()
sp1 = Sprite(orange,50,50)
sp1.rect.x =random.randint(0,480)
sp1.rect.y =random.randint(0,380)
allspritelist.add(sp1)
screen = pygame.display.set_mode(400,500)
pygame.display.set_caption("bounce")
bg_colour = white
screen.fill(bg_colour)
exit = False
clock = pygame.time.clock()
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == sprite_colour_change_event:
            sp1.change_colour()
        elif event.type == background_colour_change_event:
            change_background_colour()
    allspritelist.update()
    screen.fill(bg_colour)
    allspritelist.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()


