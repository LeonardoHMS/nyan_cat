import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Nyan Cat')
clock = pygame.time.Clock()

nyan_cat = pygame.image.load(r'nyan_cat.png')
nyan_cat_rect = nyan_cat.get_rect()

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

# Move Rainbow and Nyan Cat
    clock.tick(5)
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
    pygame.display.update()