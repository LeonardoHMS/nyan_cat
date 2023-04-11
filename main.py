from pygame.locals import QUIT
from sys import exit
import pygame

# init pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Nyan Cat')
clock = pygame.time.Clock()


def rainbow(pos, color):
    line = [(0, pos[0]), (30, pos[1]),(60, pos[1]), (90, pos[0]), (120, pos[0]), (150, pos[1])]
    line_skin = pygame.Surface((30, 15))
    line_skin.fill(color)
    for pos in line:
        screen.blit(line_skin, pos)


# Nyan Sprite
class Nyan(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load(r'sprites/nyan_cat1.png'))
        self.sprites.append(pygame.image.load(r'sprites/nyan_cat2.png'))
        self.sprites.append(pygame.image.load(r'sprites/nyan_cat3.png'))
        self.sprites.append(pygame.image.load(r'sprites/nyan_cat4.png'))
        self.sprites.append(pygame.image.load(r'sprites/nyan_cat5.png'))
        self.sprites.append(pygame.image.load(r'sprites/nyan_cat6.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (270, 150))
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 215

    def update(self):
        self.atual += 1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (270, 150))


sprites_nyan = pygame.sprite.Group()
nyan = Nyan()
sprites_nyan.add(nyan)

# Music
pygame.mixer.init()
pygame.mixer.music.load('nyan_cat_music.mp3')
pygame.mixer.music.play()

# Bomb Spawn, Valores: 3 Eixo X dps 2 Eixo Y para movimentos de explosões
bomb_pix = [
((580, 50), (590, 50),(600, 50),(590, 60),(590, 40)),
((510, 50), (570, 50),(540, 80),(540, 20)),
((480, 50), (490, 50),(500, 50),(490, 60),(490, 40)),
((410, 50), (470, 50),(440, 80),(440, 20)),
((380, 50), (390, 50),(400, 50),(390, 60),(390, 40)),
((310, 50), (370, 50),(340, 80),(340, 20)),
((280, 50), (290, 50),(300, 50),(290, 60),(290, 40)),
((210, 50), (270, 50),(240, 80),(240, 20)),
((180, 50), (190, 50),(200, 50),(190, 60),(190, 40)),
((110, 50), (170, 50),(140, 80),(140, 20)),
((80, 50), (90, 50),(100, 50),(90, 60),(90, 40)),
((10, 50), (70, 50),(40, 80),(40, 20)),
((0, 50), (10, 50),(0, 60),(0, 40))
]
bomb_pix_skin = pygame.Surface((10, 10))
bomb_pix_skin.fill((255, 250, 250))

# Lines Color
pos_red = pos_orange = pos_yellow = pos_green = pos_blue = pos_violet = loop = 0
while True:
    if loop % 2 == 0:
        pos_red = (240, 245)
        pos_orange =(255, 260)
        pos_yellow =(270, 275)
        pos_green =(285, 290)
        pos_blue =(300, 305)
        pos_violet =(315, 320)
    else:
        pos_red = (245, 240)
        pos_orange = (260, 255)
        pos_yellow = (275, 270)
        pos_green = (290, 285)
        pos_blue = (305, 300)
        pos_violet = (320, 315)
    loop += 1

# Move Rainbow and Nyan Cat and Bomb Spawn
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 128))

# Spawn bomb in the screen
    if loop % 9 == 0:
        bomb_pix1 = bomb_pix[:]
    try:
        for pos in bomb_pix1[0]:
            screen.blit(bomb_pix_skin, pos)
            screen.blit(bomb_pix_skin, (pos[0]+50,pos[1]+350))
        del (bomb_pix1[0])
    except:
        pass
    if loop % 14 == 0:
        bomb_pix2 = bomb_pix[:]
    try:
        for pos in bomb_pix2[0]:
            screen.blit(bomb_pix_skin, (pos[0]-50,pos[1]+270))
            for pos in bomb_pix2[0]:
                screen.blit(bomb_pix_skin, (pos[0]+50,pos[1]+480))
                screen.blit(bomb_pix_skin, (pos[0]-50, pos[1]+100))
        del (bomb_pix2[0])
    except:
        pass
# Rainbow
    rainbow(pos_red, (255, 0, 0))
    rainbow(pos_orange, (255, 140, 0))
    rainbow(pos_yellow, (255, 255, 0))
    rainbow(pos_green, (0, 255, 0))
    rainbow(pos_blue, (0, 0, 255))
    rainbow(pos_violet, (255, 0, 255))
# Nyan
    sprites_nyan.draw(screen)
    sprites_nyan.update()
    pygame.display.flip()
