# music player with tkinter and pygame
from tkinter import *
import sys
import pygame
from pygame.locals import QUIT

pygame.init()

# music player screen option set
size = [500, 400]
screen = pygame.display.set_mode(size)

title = "My Music Player"
pygame.display.set_caption(title)

# Setting for music player inside
clock = pygame.time.Clock()
color = (0,0,0)

# main event

SB = 0
while SB==0:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            SB = 1
            
        else:
            screen.fill(color)
        pygame.display.flip()
pygame.quit()
sys.exit()

