import pygame
import sys
from pygame.locals import *

# Initializes the system;
pygame.init()
WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Single Player Snooker Game ")


while True:  # main game loop;           
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
