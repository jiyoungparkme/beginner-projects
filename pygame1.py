import pygame
import sys
import time
import random

from pygame.locals import *

WINDOW_WIDTH =800
WINDOW_HEIGHT = 600

WHITHE = (255,255,255)

if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0 , 32)
    pygame.display.set_caption("Python Game")
    surface = pygame.Surface(sindow.get_size())
    surface = surface.convert()
    surface.fill(WHITE)
    clock = pygame.time.Clock()
    pygame.key_set_repeat(1,40)
    window.blit(surface, (0,0))
