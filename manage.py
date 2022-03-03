import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Nyan Cat')
clock = pygame.time.Clock()

# Lines Color
surface = (15, 15)
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

    line_red = [(0, pos_red[0]), (10, pos_red[0]), (20, pos_red[0]),(30, pos_red[1]),(40, pos_red[1]),(50, pos_red[1]), (60, pos_red[1]), (70, pos_red[1]), (80, pos_red[0]), (90, pos_red[0]), (100, pos_red[0]), (110, pos_red[0]), (120, pos_red[0]), (130, pos_red[1]), (140, pos_red[1]), (150, pos_red[1]), (160, pos_red[1]), (170, pos_red[1])]
    line_red_skin = pygame.Surface(surface)
    line_red_skin.fill((255,0,0))

    line_orange = [(0, pos_orange[0]), (10, pos_orange[0]), (20, pos_orange[0]),(30, pos_orange[1]),(40, pos_orange[1]),(50, pos_orange[1]), (60, pos_orange[1]), (70, pos_orange[1]), (80, pos_orange[0]), (90, pos_orange[0]), (100, pos_orange[0]), (110, pos_orange[0]), (120, pos_orange[0]), (130, pos_orange[1]), (140, pos_orange[1]), (150, pos_orange[1]), (160, pos_orange[1]), (170, pos_orange[1])]
    line_orange_skin = pygame.Surface(surface)
    line_orange_skin.fill((255,140,0))

    line_yellow = [(0, pos_yellow[0]), (10, pos_yellow[0]), (20, pos_yellow[0]),(30, pos_yellow[1]),(40, pos_yellow[1]),(50, pos_yellow[1]), (60, pos_yellow[1]), (70, pos_yellow[1]), (80, pos_yellow[0]), (90, pos_yellow[0]), (100, pos_yellow[0]), (110, pos_yellow[0]), (120, pos_yellow[0]), (130, pos_yellow[1]), (140, pos_yellow[1]), (150, pos_yellow[1]), (160, pos_yellow[1]), (170, pos_yellow[1])]
    line_yellow_skin = pygame.Surface(surface)
    line_yellow_skin.fill((255,255,0))

    line_green = [(0, pos_green[0]), (10, pos_green[0]), (20, pos_green[0]),(30, pos_green[1]),(40, pos_green[1]),(50, pos_green[1]), (60, pos_green[1]), (70, pos_green[1]), (80, pos_green[0]), (90, pos_green[0]), (100, pos_green[0]), (110, pos_green[0]), (120, pos_green[0]), (130, pos_green[1]), (140, pos_green[1]), (150, pos_green[1]), (160, pos_green[1]), (170, pos_green[1])]
    line_green_skin = pygame.Surface(surface)
    line_green_skin.fill((0,255,0))

    line_blue = [(0, pos_blue[0]), (10, pos_blue[0]), (20, pos_blue[0]),(30, pos_blue[1]),(40, pos_blue[1]),(50, pos_blue[1]), (60, pos_blue[1]), (70, pos_blue[1]), (80, pos_blue[0]), (90, pos_blue[0]), (100, pos_blue[0]), (110, pos_blue[0]), (120, pos_blue[0]), (130, pos_blue[1]), (140, pos_blue[1]), (150, pos_blue[1]), (160, pos_blue[1]), (170, pos_blue[1])]
    line_blue_skin = pygame.Surface(surface)
    line_blue_skin.fill((0,0,255))

    line_violet = [(0, pos_violet[0]), (10, pos_violet[0]), (20, pos_violet[0]),(30, pos_violet[1]),(40, pos_violet[1]),(50, pos_violet[1]), (60, pos_violet[1]), (70, pos_violet[1]), (80, pos_violet[0]), (90, pos_violet[0]), (100, pos_violet[0]), (110, pos_violet[0]), (120, pos_violet[0]), (130, pos_violet[1]), (140, pos_violet[1]), (150, pos_violet[1]), (160, pos_violet[1]), (170, pos_violet[1])]
    line_violet_skin = pygame.Surface(surface)
    line_violet_skin.fill((255,0,255))

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
    pygame.display.update()