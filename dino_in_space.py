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

    def update(self, key_pressed):
        if key_pressed[pygame.K_UP]:
            self.rect.move_ip(0, -5)

        if key_pressed[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)

        if key_pressed[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)

        if key_pressed[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        
d1 = Dino(200, 200)
d2 = Dino(300, 300)
d3 = Dino(100, 100)
d4 = Dino(400, 400)
d5 = Dino(500, 500)
dino_grp = pygame.sprite.Group()
dino_grp.add(d1, d2, d3, d4, d5)

while True:
    screen.fill("white")
    dino_grp.draw(screen)
    key_pressed = pygame.key.get_pressed()
    d1.update(key_pressed)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
