from pygame.locals import QUIT
from sys import exit
import pygame

# init pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Nyan Cat')
clock = pygame.time.Clock()


def rainbow(pos, color):
    line = [
        (0, pos[0]),
        (30, pos[1]),
        (60, pos[1]),
        (90, pos[0]),
        (120, pos[0]),
        (150, pos[1])
        ]
    line_skin = pygame.Surface((30, 15))
    line_skin.fill(color)
    for pos in line:
        screen.blit(line_skin, pos)


class Stars():
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.bomb_pix = []
        self.bomb_pix_skin = pygame.Surface((10, 10))
        self.bomb_pix_skin.fill((255, 250, 250))

    def _list_pixels(self, pos_x, pos_y):
        while pos_x > 0:
            self.bomb_pix.append((
                (pos_x, 50+pos_y), (pos_x+10, 50+pos_y), (pos_x+20, 50+pos_y), (pos_x+10, 60+pos_y), (pos_x+10, 40+pos_y) # noqa
            ))
            self.bomb_pix.append((
                (pos_x-70, 50+pos_y), (pos_x-10, 50+pos_y), (pos_x-40, 80+pos_y), (pos_x-40, 20+pos_y) # noqa
            ))
            pos_x -= 100

    def update(self):
        if len(self.bomb_pix) == 0:
            Stars._list_pixels(self, self.pos_x, self.pos_y)
        for pos in self.bomb_pix[0]:
            screen.blit(self.bomb_pix_skin, pos)
        del (self.bomb_pix[0])


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


star_1 = Stars(680, 0)
star_2 = Stars(830, 100)
star_3 = Stars(720, 300)
star_4 = Stars(980, 350)
star_5 = Stars(850, 480)

sprites_nyan = pygame.sprite.Group()  # type: ignore
nyan = Nyan()
sprites_nyan.add(nyan)

# Music
pygame.mixer.init()
pygame.mixer.music.load('nyan_cat_music.mp3')
pygame.mixer.music.play()

# Lines Color
pos_red = pos_orange = pos_yellow = pos_green = pos_blue = pos_violet = loop = 0  # noqa
while True:
    if loop % 2 == 0:
        pos_red = (240, 245)  # type: ignore
        pos_orange = (255, 260)  # type: ignore
        pos_yellow = (270, 275)  # type: ignore
        pos_green = (285, 290)  # type: ignore
        pos_blue = (300, 305)  # type: ignore
        pos_violet = (315, 320)  # type: ignore
    else:
        pos_red = (245, 240)  # type: ignore
        pos_orange = (260, 255)  # type: ignore
        pos_yellow = (275, 270)  # type: ignore
        pos_green = (290, 285)  # type: ignore
        pos_blue = (305, 300)  # type: ignore
        pos_violet = (320, 315)  # type: ignore
    loop += 1

# Move Rainbow, Nyan and Stars
    clock.tick(8)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    screen.fill((0, 0, 128))

# Spawn stars in the screen
    star_1.update()
    star_2.update()
    star_3.update()
    star_4.update()
    star_5.update()

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
