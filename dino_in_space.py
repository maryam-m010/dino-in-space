import pygame, sys

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("dino in space")
screen.fill("white")

pygame.display.update()

class Dino(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("dino.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

d1 = Dino(200, 200)
dino_grp = pygame.sprite.Group()
dino_grp.add(d1)

while True:
    dino_grp.draw(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()