import pygame
from pygame.locals import *

# init pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Nyan Cat')
clock = pygame.time.Clock()

nyan_cat = pygame.image.load(r'nyan_cat.png')
nyan_cat_rect = nyan_cat.get_rect()

# Music
pygame.mixer.init()
pygame.mixer.music.load('nyan_cat_music.mp3')
pygame.mixer.music.play()

#Bomb Spawn, Valores: 3 Eixo X dps 2 Eixo Y para movimentos de explosões
bomb_pix_1 = [
((580, 50),(590, 50),(600, 50),(590, 60),(590, 40)),
((510, 50),(570, 50),(540, 80),(540, 20)),
((480, 50),(490, 50),(500, 50),(490, 60),(490, 40)),
((410, 50),(470, 50),(440, 80),(440, 20)),
((380, 50),(390, 50),(400, 50),(390, 60),(390, 40)),
((310, 50),(370, 50),(340, 80),(340, 20)),
((280, 50),(290, 50),(300, 50),(290, 60),(290, 40)),
((210, 50),(270, 50),(240, 80),(240, 20)),
((180, 50),(190, 50),(200, 50),(190, 60),(190, 40)),
((110, 50),(170, 50),(140, 80),(140, 20)),
((80, 50),(90, 50),(100, 50),(90, 60),(90, 40)),
((10, 50),(70, 50),(40, 80),(40, 20)),
((0, 50),(10, 50),(0, 60),(0, 40))
]
bomb_pix_skin_1 = pygame.Surface((10,10))
bomb_pix_skin_1.fill((255,250,250))

bomb_pix_2 = [
((580, 150),(590, 150),(600, 150),(590, 160),(590, 140)),
((510, 150),(570, 150),(540, 180),(540, 120)),
((480, 150),(490, 150),(500, 150),(490, 160),(490, 140)),
((410, 150),(470, 150),(440, 180),(440, 120)),
((380, 150),(390, 150),(400, 150),(390, 160),(390, 140)),
((310, 150),(370, 150),(340, 180),(340, 120)),
((280, 150),(290, 150),(300, 150),(290, 160),(290, 140)),
((210, 150),(270, 150),(240, 180),(240, 120)),
((180, 150),(190, 150),(200, 150),(190, 160),(190, 140)),
((110, 150),(170, 150),(140, 180),(140, 120)),
((80, 150),(90, 150),(100, 150),(90, 160),(90, 140)),
((10, 150),(70, 150),(40, 180),(40, 120)),
((0, 150),(10, 150),(0, 160),(0, 140))
]
bomb_pix_skin_2 = pygame.Surface((10,10))
bomb_pix_skin_2.fill((255,250,250))
# Lines Color
surface = (30, 15)
pos_red = pos_orange = pos_yellow = pos_green = pos_blue = pos_violet = loop = 0
while True:
    if loop % 2 == 0:
        pos_red = (240, 245)
        pos_orange = (255, 260)
        pos_yellow = (270, 275)
        pos_green = (285, 290)
        pos_blue = (300, 305)
        pos_violet = (315, 320)
    else:
        pos_red = (245, 240)
        pos_orange = (260, 255)
        pos_yellow = (275, 270)
        pos_green = (290, 285)
        pos_blue = (305, 300)
        pos_violet = (320, 315)
    loop += 1

    line_red = [(0, pos_red[0]), (30, pos_red[1]),(60, pos_red[1]), (90, pos_red[0]), (120, pos_red[0]), (150, pos_red[1])]
    line_red_skin = pygame.Surface(surface)
    line_red_skin.fill((255,0,0))

    line_orange = [(0, pos_orange[0]), (30, pos_orange[1]),(60, pos_orange[1]), (90, pos_orange[0]), (120, pos_orange[0]), (150, pos_orange[1])]
    line_orange_skin = pygame.Surface(surface)
    line_orange_skin.fill((255,140,0))

    line_yellow = [(0, pos_yellow[0]), (30, pos_yellow[1]),(60, pos_yellow[1]), (90, pos_yellow[0]), (120, pos_yellow[0]), (150, pos_yellow[1])]
    line_yellow_skin = pygame.Surface(surface)
    line_yellow_skin.fill((255,255,0))

    line_green = [(0, pos_green[0]), (30, pos_green[1]),(60, pos_green[1]), (90, pos_green[0]), (120, pos_green[0]), (150, pos_green[1])]
    line_green_skin = pygame.Surface(surface)
    line_green_skin.fill((0,255,0))

    line_blue = [(0, pos_blue[0]), (30, pos_blue[1]),(60, pos_blue[1]), (90, pos_blue[0]), (120, pos_blue[0]), (150, pos_blue[1])]
    line_blue_skin = pygame.Surface(surface)
    line_blue_skin.fill((0,0,255))

    line_violet = [(0, pos_violet[0]), (30, pos_violet[1]),(60, pos_violet[1]), (90, pos_violet[0]), (120, pos_violet[0]), (150, pos_violet[1])]
    line_violet_skin = pygame.Surface(surface)
    line_violet_skin.fill((255,0,255))

# Move Rainbow and Nyan Cat and Bomb Spawn
    clock.tick(4)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    screen.fill((0,0,0))
    for pos in line_red:
        screen.blit(line_red_skin, pos)
    for pos in line_orange:
        screen.blit(line_orange_skin, pos)
    for pos in line_yellow:
        screen.blit(line_yellow_skin, pos)
    for pos in line_green:
        screen.blit(line_green_skin, pos)
    for pos in line_blue:
        screen.blit(line_blue_skin, pos)
    for pos in line_violet:
        screen.blit(line_violet_skin, pos)
    screen.blit(nyan_cat, (80, 190))
# Spawn bomb in the screen
    if loop % 15 == 0:
        bomb_pix_1_loop = bomb_pix_1[:]
    try:
        for pos in bomb_pix_1_loop[0]:
            screen.blit(bomb_pix_skin_1, pos)
        del(bomb_pix_1_loop[0])
    except:
        pass
    if loop % 16 == 0:
        bomb_pix_2_loop = bomb_pix_2[:]
    try:
        for pos in bomb_pix_2_loop[0]:
            screen.blit(bomb_pix_skin_2, pos)
        del (bomb_pix_2_loop[0])
    except:
        pass
    pygame.display.update()